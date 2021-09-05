from musiclib.types.sounds import Sounds
from .context import MajorScale, MinorScale, scale_comparator
import pytest


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
