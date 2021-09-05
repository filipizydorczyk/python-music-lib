import pytest
from musiclib.types.sounds import Sounds
from .context import (
    AlgerianScales,
    WholeToneScale,
    ArabicScale,
    AugmentedScale,
    BalineseScale,
    ByzantineScale,
    ChineseScale,
    scale_comparator
)


def test_algerian_scale():
    assert scale_comparator(AlgerianScales(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.FIS, Sounds.G,
                             Sounds.GIS, Sounds.B})


def test_algerian_scale_over_ocateve():
    assert scale_comparator(AlgerianScales(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.AIS,
                             Sounds.C, Sounds.CIS, Sounds.D,
                             Sounds.DIS, Sounds.FIS})


def test_whole_tone_1_scale():
    assert scale_comparator(WholeToneScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E,
                             Sounds.FIS, Sounds.GIS, Sounds.AIS})


def test_whole_tone_2_scale():
    assert scale_comparator(WholeToneScale(Sounds.CIS),
                            {Sounds.CIS, Sounds.DIS, Sounds.F,
                             Sounds.G, Sounds.A, Sounds.B})


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
    assert scale_comparator(ArabicScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E,
                             Sounds.F, Sounds.FIS, Sounds.GIS,
                             Sounds.AIS})


def test_arabic_scale_over_ocateve():
    assert scale_comparator(ArabicScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B,
                             Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.F})


def test_augmented_scale():
    assert scale_comparator(AugmentedScale(Sounds.C),
                            {Sounds.C, Sounds.DIS, Sounds.E,
                             Sounds.G, Sounds.GIS, Sounds.B})


def test_augmented_scale_over_ocateve():
    assert scale_comparator(AugmentedScale(Sounds.G),
                            {Sounds.G, Sounds.AIS, Sounds.B,
                             Sounds.D, Sounds.DIS, Sounds.FIS})


def test_balinese_scale():
    assert scale_comparator(BalineseScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.G, Sounds.GIS})


def test_balinese_scale_over_ocateve():
    assert scale_comparator(BalineseScale(Sounds.G),
                            {Sounds.G, Sounds.GIS, Sounds.AIS,
                             Sounds.D, Sounds.DIS})


def test_byzantine_scale():
    assert scale_comparator(ByzantineScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.E,
                             Sounds.F, Sounds.G, Sounds.GIS, Sounds.B})


def test_byzantine_scale_over_ocateve():
    assert scale_comparator(ByzantineScale(Sounds.G),
                            {Sounds.G, Sounds.GIS, Sounds.B,
                             Sounds.C, Sounds.D, Sounds.DIS, Sounds.FIS})


def test_chinese_scale():
    assert scale_comparator(ChineseScale(Sounds.C),
                            {Sounds.C, Sounds.E, Sounds.FIS,
                             Sounds.G, Sounds.B})


def test_chinese_scale_over_ocateve():
    assert scale_comparator(ChineseScale(Sounds.G),
                            {Sounds.G, Sounds.B, Sounds.CIS,
                             Sounds.D, Sounds.FIS})
