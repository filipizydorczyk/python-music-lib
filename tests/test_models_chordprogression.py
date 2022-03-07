import pytest

from musiclib.models.scales import scale

from .context import ChordProgression, ChordProgressions, MajorScale, Sounds, ChordProgressionStringFormat

def test_should_throw_wrong_string_format():
    scale = MajorScale(Sounds.C)
    with pytest.raises(ChordProgressionStringFormat):
        chord_progression = ChordProgression(scale, "XD-V-ii-B")

    with pytest.raises(ChordProgressionStringFormat):
        chord_progression = ChordProgression(scale, "iv_V_ii")

    with pytest.raises(ChordProgressionStringFormat):
        chord_progression = ChordProgression(scale, "VII-V-ii")

    with pytest.raises(ChordProgressionStringFormat):
        chord_progression = ChordProgression(scale, "I--V-vi-IV")

def test_should_create_with_predefined_enum():
    scale = MajorScale(Sounds.C)
    chord_progression = ChordProgression(scale, ChordProgressions.I_V_vi_IV)
    assert len(chord_progression.get_chords_list()) == 4

def test_should_create_with_correctly_formated_string():
    scale = MajorScale(Sounds.C)
    chord_progression = ChordProgression(scale, "V-iii-IV-I")
    assert len(chord_progression.get_chords_list()) == 4