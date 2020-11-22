import pytest
from .context import Pitch, Sounds, Intervals


def test_adding_intervals_to_pitch():
    pitch = Pitch(Sounds.A, 3)
    assert pitch.add(Intervals.MAJOR_THIRD).get_octave() == 4
    assert pitch.add(Intervals.MAJOR_THIRD).get_sound() == Sounds.CIS

    assert pitch.add(Intervals.PERFECT_FOURTH).get_octave() == 4
    assert pitch.add(Intervals.PERFECT_FOURTH).get_sound() == Sounds.D

    assert pitch.add(Intervals.PERFECT_FOURTH).get_octave() == 4
    assert pitch.add(Intervals.PERFECT_FOURTH).get_sound() == Sounds.D

    assert pitch.add(Intervals.TRITONE).get_octave() == 4
    assert pitch.add(Intervals.TRITONE).get_sound() == Sounds.DIS

    assert pitch.add(Intervals.PERFECT_FIFTH).get_octave() == 4
    assert pitch.add(Intervals.PERFECT_FIFTH).get_sound() == Sounds.E

    assert pitch.add(Intervals.MINOR_SIXTH).get_octave() == 4
    assert pitch.add(Intervals.MINOR_SIXTH).get_sound() == Sounds.F

    assert pitch.add(Intervals.MAJOR_SIXTH).get_octave() == 4
    assert pitch.add(Intervals.MAJOR_SIXTH).get_sound() == Sounds.FIS

    assert pitch.add(Intervals.MINOR_SEVENTH).get_octave() == 4
    assert pitch.add(Intervals.MINOR_SEVENTH).get_sound() == Sounds.G

    assert pitch.add(Intervals.MAJOR_SEVENTH).get_octave() == 4
    assert pitch.add(Intervals.MAJOR_SEVENTH).get_sound() == Sounds.GIS

    assert pitch.add(Intervals.PERFECT_OCTAVE).get_octave() == 4
    assert pitch.add(Intervals.PERFECT_OCTAVE).get_sound() == Sounds.A


def test_adding_semitones_to_pitch():
    pitch = Pitch(Sounds.A, 3)
    assert pitch.add(1).get_octave() == 3
    assert pitch.add(1).get_sound() == Sounds.AIS

    assert pitch.add(12).get_octave() == 4
    assert pitch.add(12).get_sound() == Sounds.A

    assert pitch.add(25).get_octave() == 5
    assert pitch.add(25).get_sound() == Sounds.AIS

    assert pitch.add(14).get_octave() == 4
    assert pitch.add(14).get_sound() == Sounds.B

    assert pitch.add(27).get_octave() == 6
    assert pitch.add(27).get_sound() == Sounds.C

    assert pitch.add(16).get_octave() == 5
    assert pitch.add(16).get_sound() == Sounds.CIS

    assert pitch.add(29).get_octave() == 6
    assert pitch.add(29).get_sound() == Sounds.D

    assert pitch.add(18).get_octave() == 5
    assert pitch.add(18).get_sound() == Sounds.DIS

    assert pitch.add(31).get_octave() == 6
    assert pitch.add(31).get_sound() == Sounds.E

    assert pitch.add(20).get_octave() == 5
    assert pitch.add(20).get_sound() == Sounds.F

    assert pitch.add(33).get_octave() == 6
    assert pitch.add(33).get_sound() == Sounds.FIS

    assert pitch.add(22).get_octave() == 5
    assert pitch.add(22).get_sound() == Sounds.G
