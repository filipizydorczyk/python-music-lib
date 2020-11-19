import pytest
from .context import Pitch, Sounds, Intervals


def test_adding_semitones_to_pitch():
    pitch = Pitch(Sounds.DIS, 3)
    print(pitch.add(Intervals.MAJOR_THIRD).get_octave(),
          pitch.add(Intervals.MAJOR_THIRD).get_sound())
