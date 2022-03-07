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
