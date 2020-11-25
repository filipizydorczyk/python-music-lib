import pytest
from .context import createMajorChord, Pitch, Sounds


def test_create_by_semitones():
    p = Pitch(Sounds.A, 4)
    chord = createMajorChord(p)
    print(chord.get_pitches()[0].get_sound())
    print(chord.get_pitches()[1].get_sound())
    print(chord.get_pitches()[2].get_sound())
