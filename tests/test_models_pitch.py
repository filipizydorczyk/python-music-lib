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


def test_pitch_eq_and_ne():
    assert Pitch(Sounds.A, 4) == Pitch(Sounds.A, 4)
    assert (Pitch(Sounds.A, 4) != Pitch(Sounds.A, 4)) == False
    assert Pitch(Sounds.A, 5) != Pitch(Sounds.A, 4)
    assert Pitch(Sounds.A, 4) != Pitch(Sounds.AIS, 4)
    assert (Pitch(Sounds.A, 5) == Pitch(Sounds.A, 4)) == False
    assert (Pitch(Sounds.A, 4) == Pitch(Sounds.AIS, 4)) == False


def test_pitch_getting_midi_code():
    assert Pitch(Sounds.C, 4).get_midi_code() == 60
    assert Pitch(Sounds.C, -1).get_midi_code() == 0
    assert Pitch(Sounds.C, 0).get_midi_code() == 12

    assert Pitch(Sounds.CIS, 4).get_midi_code() == 61
    assert Pitch(Sounds.CIS, -1).get_midi_code() == 1
    assert Pitch(Sounds.CIS, 9).get_midi_code() == 121

    assert Pitch(Sounds.D, 4).get_midi_code() == 62
    assert Pitch(Sounds.D, -1).get_midi_code() == 2
    assert Pitch(Sounds.D, 8).get_midi_code() == 110

    assert Pitch(Sounds.DIS, 4).get_midi_code() == 63
    assert Pitch(Sounds.DIS, -1).get_midi_code() == 3
    assert Pitch(Sounds.DIS, 7).get_midi_code() == 99

    assert Pitch(Sounds.E, 4).get_midi_code() == 64
    assert Pitch(Sounds.E, -1).get_midi_code() == 4
    assert Pitch(Sounds.E, 6).get_midi_code() == 88

    assert Pitch(Sounds.F, 4).get_midi_code() == 65
    assert Pitch(Sounds.F, -1).get_midi_code() == 5
    assert Pitch(Sounds.F, 5).get_midi_code() == 77

    assert Pitch(Sounds.FIS, 4).get_midi_code() == 66
    assert Pitch(Sounds.FIS, -1).get_midi_code() == 6
    assert Pitch(Sounds.FIS, 3).get_midi_code() == 54

    assert Pitch(Sounds.G, 4).get_midi_code() == 67
    assert Pitch(Sounds.G, -1).get_midi_code() == 7
    assert Pitch(Sounds.G, 9).get_midi_code() == 127

    assert Pitch(Sounds.GIS, 4).get_midi_code() == 68
    assert Pitch(Sounds.GIS, -1).get_midi_code() == 8
    assert Pitch(Sounds.GIS, 2).get_midi_code() == 44

    assert Pitch(Sounds.A, 4).get_midi_code() == 69
    assert Pitch(Sounds.A, -1).get_midi_code() == 9
    assert Pitch(Sounds.A, 1).get_midi_code() == 33

    assert Pitch(Sounds.AIS, 4).get_midi_code() == 70
    assert Pitch(Sounds.AIS, -1).get_midi_code() == 10
    assert Pitch(Sounds.AIS, 0).get_midi_code() == 22

    assert Pitch(Sounds.B, 4).get_midi_code() == 71
    assert Pitch(Sounds.B, -1).get_midi_code() == 11
    assert Pitch(Sounds.B, 8).get_midi_code() == 119

    assert Pitch(Sounds.G, 11).get_midi_code() == None
