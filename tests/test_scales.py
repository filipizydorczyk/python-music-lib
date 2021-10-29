from musiclib.types.scaletypes import ScaleTypes
from musiclib.types.sounds import Sounds
from .context import MajorScale, MinorScale, scale_comparator, IwatoScale, BalineseScale, DiminishedScale, EightToneSpanishScale, MinorPentatonicScale
import pytest


def test_get_scale_type_method():
    assert IwatoScale(Sounds.C).get_scale_type() == ScaleTypes.PENTATONIC
    assert MajorScale(Sounds.C).get_scale_type() == ScaleTypes.HEPTATONIC
    assert MinorScale(Sounds.C).get_scale_type() == ScaleTypes.HEPTATONIC
    assert BalineseScale(Sounds.C).get_scale_type() == ScaleTypes.PENTATONIC
    assert DiminishedScale(Sounds.C).get_scale_type() == ScaleTypes.OCTATONIC
    assert EightToneSpanishScale(
        Sounds.C).get_scale_type() == ScaleTypes.OCTATONIC


def test_major_scale():
    assert scale_comparator(MajorScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E,
                             Sounds.F, Sounds.G, Sounds.A, Sounds.B})


def test_major_scale_over_ocatve():
    assert scale_comparator(MajorScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B,
                             Sounds.C, Sounds.D, Sounds.E, Sounds.FIS})


def test_minor_scale():
    assert scale_comparator(MinorScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.G, Sounds.GIS, Sounds.AIS})


def test_minor_scale_over_octave():
    assert scale_comparator(MinorScale(Sounds.A),
                            {Sounds.A, Sounds.B, Sounds.C,
                             Sounds.D, Sounds.E, Sounds.F, Sounds.G})


def test_minor_pentatonic_scale_over_octave():
    assert scale_comparator(MinorPentatonicScale(Sounds.A),
                            {Sounds.A, Sounds.C,
                             Sounds.D, Sounds.E, Sounds.G, })
