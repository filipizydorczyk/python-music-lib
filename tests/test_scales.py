import pytest
from musiclib.types.notesorder import NotesOrder
from musiclib.types.scaletypes import ScaleTypes
from musiclib.types.sounds import Sounds
from .context import (
    MajorScale,
    MinorScale,
    scale_comparator,
    IwatoScale,
    BalineseScale,
    DiminishedScale,
    EightToneSpanishScale,
    MinorPentatonicScale,
    MajorPentatonicScale,
    PentatonicScale,
    NaturalMinorScale,
    MelodicMinorScale,
    HarmonicMinorScale
)

def test_get_scale_sounds_list():
    assert len(MajorPentatonicScale(Sounds.C).get_scale_sounds_list()) == 5
    assert len(MajorScale(Sounds.C).get_scale_sounds_list()) == 7
    assert len(NaturalMinorScale(Sounds.C).get_scale_sounds_list()) == 7
    assert len(MelodicMinorScale(Sounds.C).get_scale_sounds_list()) == 7

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
    assert scale_comparator(NaturalMinorScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.G, Sounds.GIS, Sounds.AIS})


def test_default_minor_scale():
    assert scale_comparator(MinorScale(Sounds.C),
                            NaturalMinorScale(Sounds.C).get_scale_sounds())


def test_minor_scale_over_octave():
    assert scale_comparator(NaturalMinorScale(Sounds.A),
                            {Sounds.A, Sounds.B, Sounds.C,
                             Sounds.D, Sounds.E, Sounds.F, Sounds.G})


def test_minor_pentatonic_scale_over_octave():
    assert scale_comparator(MinorPentatonicScale(Sounds.A),
                            {Sounds.A, Sounds.C,
                             Sounds.D, Sounds.E, Sounds.G, })


def test_major_pentatonic_scale_over_octave():
    assert scale_comparator(MajorPentatonicScale(Sounds.E),
                            {Sounds.E, Sounds.FIS,
                             Sounds.GIS, Sounds.B, Sounds.CIS, })


def test_minor_pentatonic_scale_should_be_default():
    assert scale_comparator(MinorPentatonicScale(Sounds.E),
                            PentatonicScale(Sounds.E).get_scale_sounds())


def test_melodic_minor_scale_ascending():
    assert scale_comparator(MelodicMinorScale(
        Sounds.E,
        notes_order=NotesOrder.ASCENDING
    ),
        {Sounds.E, Sounds.FIS, Sounds.G,
         Sounds.A, Sounds.B, Sounds.CIS, Sounds.DIS})


def test_melodic_minor_scale_descending():
    assert scale_comparator(MelodicMinorScale(
        Sounds.E,
        notes_order=NotesOrder.DESCENDING
    ),
        {Sounds.E, Sounds.FIS, Sounds.G,
         Sounds.A, Sounds.B, Sounds.C, Sounds.D})


def test_harmonic_minor_scale_should_be_default():
    assert scale_comparator(HarmonicMinorScale(Sounds.E),
                            {Sounds.E, Sounds.FIS, Sounds.G,
                             Sounds.A, Sounds.B, Sounds.C, Sounds.DIS})
