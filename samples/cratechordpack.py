from musiclib.models.pitch import Pitch
from mido import Message, MidiFile, MidiTrack
from musiclib import Sounds, create, Chords, Chord, Pitch


def save_chord_to_midi(chord: Chord, chord_type: Chords):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    for pitch in chord.get_pitches():
        track.append(
            Message('note_on', note=pitch.get_midi_code(), velocity=64, time=0))

    index = 0
    for pitch in chord.get_pitches():
        if(index == 0):
            track.append(
                Message('note_off', note=pitch.get_midi_code(), velocity=127, time=128))
        else:
            track.append(
                Message('note_off', note=pitch.get_midi_code(), velocity=127, time=0))
        index += 1

    mid.save(str(chord.get_pitches()[0].get_sound()
                 ) + '-' + str(chord_type) + '.mid')


for chord_type in [Chords.MAJOR, Chords.MINOR]:
    for sound in Sounds:
        if sound != Sounds.REST:
            chord = create(Pitch(sound, 4), chord_type)
            save_chord_to_midi(chord, chord_type)
