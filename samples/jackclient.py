from musiclib.models.pitch import Pitch
from musiclib.types.sounds import Sounds
from musiclib.clients.jack import MidiProcessJack
from musiclib.utils.chordsfactory import createMinorChord, createMajorChord

client = MidiProcessJack()


@client.set_process_data
def create_chord(status, pitch: Pitch, vel):
    chord = createMajorChord(pitch)

    response = []

    print("Chord")
    for ptch in chord.get_pitches():
        print(ptch)
        response.append((status, ptch, vel))

    return response


with client:
    input()
