from musiclib.types.sounds import Sounds
from .context import MajorScale, MinorScale
import pytest


def test_major_scale():
    desired_result = {Sounds.C, Sounds.D, Sounds.E,
                      Sounds.F, Sounds.G, Sounds.A, Sounds.B}

    scale = MajorScale(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_major_scale_over_ocatve():
    desired_result = {Sounds.G, Sounds.A, Sounds.B,
                      Sounds.C, Sounds.D, Sounds.E, Sounds.FIS}

    scale = MajorScale(Sounds.G)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_minor_scale():
    desired_result = {Sounds.C, Sounds.D, Sounds.DIS,
                      Sounds.F, Sounds.G, Sounds.GIS, Sounds.AIS}

    scale = MinorScale(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_minor_scale_over_octave():
    desired_result = {Sounds.A, Sounds.B, Sounds.C,
                      Sounds.D, Sounds.E, Sounds.F, Sounds.G}

    scale = MinorScale(Sounds.A)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0
