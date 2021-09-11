from musiclib.types.intervals import Intervals
import pytest
from .context import Sounds


def test_correct_values():
    assert int(Sounds.REST) == 0
    assert int(Sounds.C) == 1
    assert int(Sounds.CIS) == 2
    assert int(Sounds.D) == 3
    assert int(Sounds.DIS) == 4
    assert int(Sounds.E) == 5
    assert int(Sounds.F) == 6
    assert int(Sounds.FIS) == 7
    assert int(Sounds.G) == 8
    assert int(Sounds.GIS) == 9
    assert int(Sounds.A) == 10
    assert int(Sounds.AIS) == 11
    assert int(Sounds.B) == 12


def test_adding_semitones():
    sound = Sounds.C
    assert sound.add(0) == Sounds.C
    assert sound.add(2) == Sounds.D
    assert sound.add(3) == Sounds.DIS
    assert sound.add(6) == Sounds.FIS
    assert sound.add(7) == Sounds.G
    assert sound.add(10) == Sounds.AIS
    assert sound.add(11) == Sounds.B


def test_adding_intervals():
    sound = Sounds.C
    assert sound.add(Intervals.PERFECT_UNISON) == Sounds.C
    assert sound.add(Intervals.MAJOR_SECOND) == Sounds.D
    assert sound.add(Intervals.MINOR_THIRD) == Sounds.DIS
    assert sound.add(Intervals.DIMINISHED_FIFTH) == Sounds.FIS
    assert sound.add(Intervals.PERFECT_FIFTH) == Sounds.G
    assert sound.add(Intervals.MINOR_SEVENTH) == Sounds.AIS
    assert sound.add(Intervals.MAJOR_SEVENTH) == Sounds.B


def test_adding_intervals_over_octave():
    sound = Sounds.B
    assert sound.add(Intervals.PERFECT_UNISON) == Sounds.B
    assert sound.add(Intervals.MAJOR_SECOND) == Sounds.CIS
    assert sound.add(Intervals.MINOR_THIRD) == Sounds.D
    assert sound.add(Intervals.DIMINISHED_FIFTH) == Sounds.F
    assert sound.add(Intervals.PERFECT_FIFTH) == Sounds.FIS
    assert sound.add(Intervals.MINOR_SEVENTH) == Sounds.A
    assert sound.add(Intervals.MAJOR_SEVENTH) == Sounds.AIS


def test_adding_octaves_and_semitones():
    sound = Sounds.A
    assert sound.add(12) == Sounds.A
    assert sound.add(13) == Sounds.AIS
    assert sound.add(24) == Sounds.A
    assert sound.add(25) == Sounds.AIS
    assert sound.add(48) == Sounds.A
    assert sound.add(49) == Sounds.AIS
    assert sound.add(50) == Sounds.B
    assert sound.add(14) == Sounds.B
    assert sound.add(16) == Sounds.CIS
    assert sound.add(19) == Sounds.E
    assert sound.add(20) == Sounds.F
    assert sound.add(22) == Sounds.G


def test_adding_to_rest_should_not_perform():
    assert Sounds.REST.add(43) == Sounds.REST


def test_should_never_return_rest():
    sound = Sounds.C
    for i in range(100):
        assert sound.add(i) != Sounds.REST


def test_str_method():
    assert str(Sounds.A) == "A"
    assert str(Sounds.AIS) == "AIS"
    assert str(Sounds.B) == "B"
    assert str(Sounds.C) == "C"
    assert str(Sounds.CIS) == "CIS"
    assert str(Sounds.D) == "D"
    assert str(Sounds.DIS) == "DIS"
    assert str(Sounds.E) == "E"
    assert str(Sounds.F) == "F"
    assert str(Sounds.FIS) == "FIS"
    assert str(Sounds.G) == "G"
    assert str(Sounds.GIS) == "GIS"


def test_substract_method_basic():
    assert Sounds.A.subtract(1) == Sounds.GIS
    assert Sounds.AIS.subtract(2) == Sounds.GIS
    assert Sounds.B.subtract(1) == Sounds.AIS
    assert Sounds.CIS.subtract(1) == Sounds.C
    assert Sounds.D.subtract(1) == Sounds.CIS
    assert Sounds.DIS.subtract(3) == Sounds.C
    assert Sounds.E.subtract(1) == Sounds.DIS
    assert Sounds.F.subtract(1) == Sounds.E
    assert Sounds.G.subtract(5) == Sounds.D
    assert Sounds.GIS.subtract(6) == Sounds.D


def test_substract_method_passing_cycle():
    assert Sounds.C.subtract(1) == Sounds.B
    assert Sounds.C.subtract(2) == Sounds.AIS
    assert Sounds.C.subtract(3) == Sounds.A
    assert Sounds.C.subtract(4) == Sounds.GIS
    assert Sounds.C.subtract(5) == Sounds.G
    assert Sounds.C.subtract(6) == Sounds.FIS


def test_substract_method_octaves():
    assert Sounds.C.subtract(13) == Sounds.B
    assert Sounds.C.subtract(26) == Sounds.AIS
    assert Sounds.C.subtract(39) == Sounds.A

    assert Sounds.C.subtract(0) == Sounds.C
    assert Sounds.C.subtract(12) == Sounds.C
    assert Sounds.C.subtract(24) == Sounds.C


def test_substract_method_should_never_return_rest():
    sound = Sounds.C
    for i in range(100):
        assert sound.subtract(i) != Sounds.REST


def test_substract_method_should_always_return_rest():
    sound = Sounds.REST
    for i in range(100):
        assert sound.subtract(i) == Sounds.REST


def test_sharp_method():
    assert Sounds.C.sharp() == Sounds.CIS
    assert Sounds.D.sharp() == Sounds.DIS
    assert Sounds.E.sharp() == Sounds.F
    assert Sounds.F.sharp() == Sounds.FIS
    assert Sounds.G.sharp() == Sounds.GIS
    assert Sounds.A.sharp() == Sounds.AIS
    assert Sounds.B.sharp() == Sounds.C


def test_flat_method():
    assert Sounds.C.flat() == Sounds.B
    assert Sounds.D.flat() == Sounds.CIS
    assert Sounds.E.flat() == Sounds.DIS
    assert Sounds.F.flat() == Sounds.E
    assert Sounds.G.flat() == Sounds.FIS
    assert Sounds.A.flat() == Sounds.GIS
    assert Sounds.B.flat() == Sounds.AIS
