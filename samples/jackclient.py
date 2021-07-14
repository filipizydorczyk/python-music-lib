"""
Example how to use jack client. This example takes midi input and create major chord based on incoming pitch. 
"""

from musiclib.models.pitch import Pitch
from musiclib.types.sounds import Sounds
from musiclib.clients.jack import MidiProcessJack
from musiclib.utils.chordsfactory import createMinorChord, createMajorChord

client = MidiProcessJack()


@client.set_process_data
def create_chord(status, pitch: Pitch, vel):
    chord = createMajorChord(pitch)

    response = []

    for ptch in chord.get_pitches():
        print(ptch)
        response.append((status, ptch, vel))

    return response


with client:
    input()
