import pytest
from .context import Sounds, printTestHeader


def test_correct_values():
    printTestHeader("SoundsTest", "test_correct_values")
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
    assert sound.add(2) == Sounds.D
    assert sound.add(3) == Sounds.DIS
    assert sound.add(6) == Sounds.FIS
    assert sound.add(7) == Sounds.G
    assert sound.add(10) == Sounds.AIS
    assert sound.add(11) == Sounds.B


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
