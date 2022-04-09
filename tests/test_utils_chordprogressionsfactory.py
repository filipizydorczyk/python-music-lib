import pytest

from .context import (
    create_chordprogression,
    create_chordprogression_list,
    MajorScale,
    Sounds,
    ChordProgression,
    ChordProgressions,
    ChordProgressionStringFormat
)


def test_create_chordprogression_string_positive():
    scale = MajorScale(Sounds.C)

    assert type(create_chordprogression(scale, "V-I")) is ChordProgression


def test_create_chordprogression_enum_positive():
    scale = MajorScale(Sounds.C)

    assert type(create_chordprogression(
        scale, ChordProgressions.I_V_vi_IV)) is ChordProgression


def test_create_chordprogression_negative():
    scale = MajorScale(Sounds.C)

    with pytest.raises(ChordProgressionStringFormat):
        result = create_chordprogression(scale, "V-1")


def test_create_chordprogression_list_string_positive():
    scale = MajorScale(Sounds.C)
    result = create_chordprogression_list(scale, "V-I")

    assert type(result) is list
    assert len(result) == 2


def test_create_chordprogression_list_enum_positive():
    scale = MajorScale(Sounds.C)
    result = create_chordprogression(
        scale, ChordProgressions.Im7_Vm7_IVm7_Im7)

    assert result.get_chords_list()[0].get_pitches()[0].get_sound() == Sounds.C
    assert result.get_chords_list()[0].get_pitches()[
        1].get_sound() == Sounds.DIS
    assert result.get_chords_list()[0].get_pitches()[2].get_sound() == Sounds.G
    assert result.get_chords_list()[0].get_pitches()[
        3].get_sound() == Sounds.AIS


def test_create_chordprogression_with_m7():
    scale = MajorScale(Sounds.C)
    result = create_chordprogression_list(scale, ChordProgressions.I_V_vi_IV)

    assert type(result) is list
    assert len(result) == 4


def test_create_chordprogression_list_negative():
    scale = MajorScale(Sounds.C)

    with pytest.raises(ChordProgressionStringFormat):
        result = create_chordprogression_list(scale, "V-1")
