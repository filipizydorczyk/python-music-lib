import pytest
from .context import printTestHeader, MajorChord, Chords


def test_return_correct_type():
    chord = MajorChord()
    assert chord.get_chord_type() == Chords.MAJOR
