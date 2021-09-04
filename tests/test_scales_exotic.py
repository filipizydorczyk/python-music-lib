from musiclib.types.sounds import Sounds
from .context import AlgerianScales
import pytest


def test_algerian_scale():
    desired_result = {Sounds.C, Sounds.D, Sounds.DIS,
                      Sounds.F, Sounds.FIS, Sounds.G, Sounds.GIS, Sounds.B}

    scale = AlgerianScales(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_algerian_scale_over_ocateve():
    desired_result = {Sounds.G, Sounds.A, Sounds.AIS,
                      Sounds.C, Sounds.CIS, Sounds.D, Sounds.DIS, Sounds.FIS}

    scale = AlgerianScales(Sounds.G)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0
