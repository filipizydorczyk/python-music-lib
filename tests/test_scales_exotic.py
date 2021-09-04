from musiclib.types.sounds import Sounds
from .context import AlgerianScales, WholeToneScale, ArabicScale, AugmentedScale
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


def test_whole_tone_1_scale():
    desired_result = {Sounds.C, Sounds.D, Sounds.E,
                      Sounds.FIS, Sounds.GIS, Sounds.AIS}

    scale = WholeToneScale(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_whole_tone_2_scale():
    desired_result = {Sounds.CIS, Sounds.DIS, Sounds.F,
                      Sounds.G, Sounds.A, Sounds.B}

    scale = WholeToneScale(Sounds.CIS)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_whole_tone_overlapping_1_scale():

    scale_c = WholeToneScale(Sounds.C).get_scale_sounds()
    scale_d = WholeToneScale(Sounds.D).get_scale_sounds()
    scale_e = WholeToneScale(Sounds.E).get_scale_sounds()
    scale_fis = WholeToneScale(Sounds.FIS).get_scale_sounds()
    scale_gis = WholeToneScale(Sounds.GIS).get_scale_sounds()
    scale_ais = WholeToneScale(Sounds.AIS).get_scale_sounds()

    assert len(scale_c.symmetric_difference(scale_d)) == 0
    assert len(scale_e.symmetric_difference(scale_fis)) == 0
    assert len(scale_gis.symmetric_difference(scale_ais)) == 0


def test_whole_tone_overlapping_2_scale():

    scale_cis = WholeToneScale(Sounds.CIS).get_scale_sounds()
    scale_dis = WholeToneScale(Sounds.DIS).get_scale_sounds()
    scale_f = WholeToneScale(Sounds.F).get_scale_sounds()
    scale_g = WholeToneScale(Sounds.G).get_scale_sounds()
    scale_a = WholeToneScale(Sounds.A).get_scale_sounds()
    scale_b = WholeToneScale(Sounds.B).get_scale_sounds()

    assert len(scale_cis.symmetric_difference(scale_f)) == 0
    assert len(scale_a.symmetric_difference(scale_dis)) == 0
    assert len(scale_g.symmetric_difference(scale_b)) == 0


def test_arabic_scale():
    desired_result = {Sounds.C, Sounds.D, Sounds.E,
                      Sounds.F, Sounds.FIS, Sounds.GIS, Sounds.AIS}

    scale = ArabicScale(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_arabic_scale_over_ocateve():
    desired_result = {Sounds.G, Sounds.A, Sounds.B,
                      Sounds.C, Sounds.CIS, Sounds.DIS, Sounds.F}

    scale = ArabicScale(Sounds.G)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_augmented_scale():
    desired_result = {Sounds.C, Sounds.DIS, Sounds.E,
                      Sounds.G, Sounds.GIS, Sounds.B}

    scale = AugmentedScale(Sounds.C)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0


def test_augmented_scale_over_ocateve():
    desired_result = {Sounds.G, Sounds.AIS, Sounds.B,
                      Sounds.D, Sounds.DIS, Sounds.FIS}

    scale = AugmentedScale(Sounds.G)
    actual_result = scale.get_scale_sounds()
    assert len(desired_result.symmetric_difference(actual_result)) == 0
