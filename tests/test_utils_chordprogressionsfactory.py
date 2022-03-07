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

    assert type(create_chordprogression(scale,"V-I")) is ChordProgression

def test_create_chordprogression_enum_positive():
    scale = MajorScale(Sounds.C)

    assert type(create_chordprogression(scale,ChordProgressions.I_V_vi_IV)) is ChordProgression

def test_create_chordprogression_negative():
    scale = MajorScale(Sounds.C)

    with pytest.raises(ChordProgressionStringFormat):
        result = create_chordprogression(scale,"V-1")
