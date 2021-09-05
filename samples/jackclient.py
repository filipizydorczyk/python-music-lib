"""
Example how to use jack client. This example takes midi input and create major chord based on incoming pitch. 
"""

from musiclib.models.pitch import Pitch
from musiclib.clients.jack import MidiProcessJack
from musiclib.utils.chordsfactory import create_major_chord

client = MidiProcessJack()


@client.set_process_data
def create_chord(status, pitch: Pitch, vel):
    chord = create_major_chord(pitch)

    response = []

    for ptch in chord.get_pitches():
        print(ptch)
        response.append((status, ptch, vel))

    return response


with client:
    input()
