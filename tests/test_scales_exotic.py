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
    DiminishedScale,
    DominantDiminishedScale,
    DiminishedBluesScale,
    scale_comparator,
    EgyptianScale,
    EightToneSpanishScale,
    EnigmaticMajorScale,
    EnigmaticMinorScale,
    NotesOrder,
    GeezScale,
    HawaiianScale,
    HinduScale,
    AeolianDominantScale,
    HirajoshiScale,
    HungarianMinorScale,
    HungarianGypsyScale,
    HungarianMajorScale,
    IwatoScale,
    JapaneseScale,
    Lydianb7Scale,
    LydianDominantScale,
    NeapolitanMinorScale,
    NeapolitanMajorScale,
    OctatonicHalfWholeScale
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


def test_diminished_scale():
    assert scale_comparator(DiminishedScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.FIS, Sounds.GIS,
                             Sounds.A, Sounds.B})


def test_diminished_scale_over_ocateve():
    assert scale_comparator(DiminishedScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.AIS,
                             Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.E, Sounds.FIS})


def test_dominant_diminished_scale():
    assert scale_comparator(DominantDiminishedScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.E, Sounds.FIS, Sounds.G,
                             Sounds.A, Sounds.AIS})


def test_dominant_diminished_scale_over_ocateve():
    assert scale_comparator(DominantDiminishedScale(Sounds.G),
                            {Sounds.G, Sounds.GIS, Sounds.AIS,
                             Sounds.B, Sounds.CIS, Sounds.D,
                             Sounds.E, Sounds.F})


def test_diminished_blues_is_dominant_diminished():
    for sound in Sounds:
        assert scale_comparator(DiminishedBluesScale(
            sound), DominantDiminishedScale(sound).get_scale_sounds())


def test_dominant_egyptian_scale():
    assert scale_comparator(EgyptianScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.F,
                             Sounds.G, Sounds.AIS})


def test_dominant_egyptian_scale_over_ocateve():
    assert scale_comparator(EgyptianScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.C,
                             Sounds.D, Sounds.F, Sounds.G})


def test_eight_tone_spanish_scale():
    assert scale_comparator(EightToneSpanishScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.E, Sounds.F, Sounds.FIS,
                             Sounds.GIS, Sounds.AIS})


def test_eight_tone_spanish_scale_over_ocateve():
    assert scale_comparator(EightToneSpanishScale(Sounds.G),
                            {Sounds.G, Sounds.GIS, Sounds.AIS,
                             Sounds.B, Sounds.C, Sounds.CIS,
                             Sounds.DIS, Sounds.F})


def test_enigmatic_major_scale_default_constructor():
    for sound in Sounds:
        assert scale_comparator(EnigmaticMajorScale(sound),
                                EnigmaticMajorScale(sound,
                                                    NotesOrder.ASCENDING)
                                .get_scale_sounds())


def test_enigmatic_major_scale_ascending():
    assert scale_comparator(EnigmaticMajorScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.E,
                             Sounds.FIS, Sounds.GIS, Sounds.AIS,
                             Sounds.B})


def test_enigmatic_major_scale_ascending_over_octave():
    assert scale_comparator(EnigmaticMajorScale(Sounds.G,
                                                NotesOrder.ASCENDING),
                            {Sounds.G, Sounds.GIS, Sounds.B,
                             Sounds.CIS, Sounds.DIS, Sounds.F,
                             Sounds.FIS})


def test_enigmatic_major_scale_descending():
    assert scale_comparator(EnigmaticMajorScale(Sounds.B,
                                                NotesOrder.DESCENDING),
                            {Sounds.B, Sounds.AIS, Sounds.A,
                             Sounds.G, Sounds.E, Sounds.DIS,
                             Sounds.C})


def test_enigmatic_major_scale_descending_over_octave():
    assert scale_comparator(EnigmaticMajorScale(Sounds.C,
                                                NotesOrder.DESCENDING),
                            {Sounds.C, Sounds.B, Sounds.AIS,
                             Sounds.GIS, Sounds.F, Sounds.E,
                             Sounds.CIS})


def test_enigmatic_minor_scale_descending():
    assert scale_comparator(EnigmaticMinorScale(Sounds.C),
                            {Sounds.C, Sounds.CIS, Sounds.DIS,
                             Sounds.FIS, Sounds.G, Sounds.AIS,
                             Sounds.B})


def test_enigmatic_minor_scale_descending_over_octave():
    assert scale_comparator(EnigmaticMinorScale(Sounds.G),
                            {Sounds.G, Sounds.GIS, Sounds.AIS,
                             Sounds.CIS, Sounds.D, Sounds.F,
                             Sounds.FIS})


def test_geez_scale():
    assert scale_comparator(GeezScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.G, Sounds.GIS,
                             Sounds.AIS})


def test_geez_scale_over_octave():
    assert scale_comparator(GeezScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.AIS,
                             Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F})


def test_hawaiian_scale():
    assert scale_comparator(HawaiianScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.DIS,
                             Sounds.F, Sounds.G, Sounds.A,
                             Sounds.B})


def test_hawaiian_scale_over_octave():
    assert scale_comparator(HawaiianScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.AIS,
                             Sounds.C, Sounds.D, Sounds.E,
                             Sounds.FIS})


def test_hindu_scale():
    assert scale_comparator(HinduScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E,
                             Sounds.F, Sounds.G, Sounds.A.flat(),
                             Sounds.B.flat()})


def test_hindu_scale_over_octave():
    assert scale_comparator(HinduScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B,
                             Sounds.C, Sounds.D, Sounds.E.flat(),
                             Sounds.F})


def test_aeolian_dominant_same_as_hindu_scale():
    for sound in Sounds:
        assert scale_comparator(AeolianDominantScale(sound),
                                HinduScale(sound).get_scale_sounds())


def test_hirajoshi_scale():
    assert scale_comparator(HirajoshiScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E.flat(),
                             Sounds.G, Sounds.A.flat()
                             })


def test_hirajoshi_scale_over_octave():
    assert scale_comparator(HirajoshiScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B.flat(),
                             Sounds.D, Sounds.E.flat(),
                             Sounds.G})


def test_hungarian_minor_scale():
    assert scale_comparator(HungarianMinorScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E.flat(),
                             Sounds.FIS, Sounds.G, Sounds.A.flat(),
                             Sounds.B
                             })


def test_hungarian_minor_scale_over_octave():
    assert scale_comparator(HungarianMinorScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B.flat(),
                             Sounds.CIS, Sounds.D, Sounds.E.flat(),
                             Sounds.FIS})


def test_hungarian_gypsy_scale_as_hungarian_minor():
    for sound in Sounds:
        assert scale_comparator(HungarianGypsyScale(sound),
                                HungarianMinorScale(sound).get_scale_sounds())


def test_hungarian_major_scale():
    assert scale_comparator(HungarianMajorScale(Sounds.C),
                            {Sounds.C, Sounds.DIS, Sounds.E,
                             Sounds.FIS, Sounds.G, Sounds.A,
                             Sounds.B.flat()
                             })


def test_hungarian_major_scale_over_octave():
    assert scale_comparator(HungarianMajorScale(Sounds.G),
                            {Sounds.G, Sounds.AIS, Sounds.B,
                             Sounds.CIS, Sounds.D, Sounds.E,
                             Sounds.F})


def test_iwato_scale():
    assert scale_comparator(IwatoScale(Sounds.C),
                            {Sounds.C, Sounds.D.flat(), Sounds.F,
                             Sounds.G.flat(), Sounds.B.flat()
                             })


def test_iwato_scale_over_octave():
    assert scale_comparator(IwatoScale(Sounds.G),
                            {Sounds.G, Sounds.A.flat(), Sounds.C,
                             Sounds.D.flat(), Sounds.F})


def test_japanese_scale():
    assert scale_comparator(JapaneseScale(Sounds.C),
                            {Sounds.C, Sounds.D.flat(),
                             Sounds.F, Sounds.G, Sounds.B.flat()
                             })


def test_japanese_scale_over_octave():
    assert scale_comparator(JapaneseScale(Sounds.G),
                            {Sounds.G, Sounds.A.flat(),
                             Sounds.C, Sounds.D, Sounds.F
                             })


def test_japanese_scale_reocuring():
    assert scale_comparator(JapaneseScale(Sounds.CIS),
                            JapaneseScale(Sounds.D.flat()).get_scale_sounds())
    assert scale_comparator(JapaneseScale(Sounds.DIS),
                            JapaneseScale(Sounds.E.flat()).get_scale_sounds())
    assert scale_comparator(JapaneseScale(Sounds.FIS),
                            JapaneseScale(Sounds.G.flat()).get_scale_sounds())
    assert scale_comparator(JapaneseScale(Sounds.GIS),
                            JapaneseScale(Sounds.A.flat()).get_scale_sounds())
    assert scale_comparator(JapaneseScale(Sounds.AIS),
                            JapaneseScale(Sounds.B.flat()).get_scale_sounds())


def test_lydiandominant_scale():
    assert scale_comparator(LydianDominantScale(Sounds.C),
                            {Sounds.C, Sounds.D, Sounds.E,
                             Sounds.FIS, Sounds.G, Sounds.A,
                             Sounds.B.flat()
                             })


def test_lydiandominant_scale_over_octave():
    assert scale_comparator(LydianDominantScale(Sounds.G),
                            {Sounds.G, Sounds.A, Sounds.B,
                             Sounds.CIS, Sounds.D, Sounds.E,
                             Sounds.F
                             })


def test_lydiandominantscale_scale_reocuring():
    assert scale_comparator(LydianDominantScale(Sounds.CIS),
                            LydianDominantScale(Sounds.D.flat()).get_scale_sounds())
    assert scale_comparator(LydianDominantScale(Sounds.DIS),
                            LydianDominantScale(Sounds.E.flat()).get_scale_sounds())
    assert scale_comparator(LydianDominantScale(Sounds.FIS),
                            LydianDominantScale(Sounds.G.flat()).get_scale_sounds())
    assert scale_comparator(LydianDominantScale(Sounds.GIS),
                            LydianDominantScale(Sounds.A.flat()).get_scale_sounds())
    assert scale_comparator(LydianDominantScale(Sounds.AIS),
                            LydianDominantScale(Sounds.B.flat()).get_scale_sounds())


def test_lydiandominantscale_same_as_lydianb7scale():
    for sound in Sounds:
        assert scale_comparator(LydianDominantScale(sound),
                                Lydianb7Scale(sound).get_scale_sounds())


def test_neapolitan_minor_scale():
    assert scale_comparator(NeapolitanMinorScale(Sounds.C),
                            {Sounds.C, Sounds.D.flat(), Sounds.E.flat(),
                             Sounds.F, Sounds.G, Sounds.A.flat(),
                             Sounds.B
                             })


def test_neapolitan_minor_scale_over_octave():
    assert scale_comparator(NeapolitanMinorScale(Sounds.G),
                            {Sounds.G, Sounds.A.flat(), Sounds.B.flat(),
                             Sounds.C, Sounds.D, Sounds.E.flat(),
                             Sounds.FIS
                             })


def test_neapolitan_major_scale():
    assert scale_comparator(NeapolitanMajorScale(Sounds.C),
                            {Sounds.C, Sounds.D.flat(), Sounds.E.flat(),
                             Sounds.F, Sounds.G, Sounds.A, Sounds.B
                             })


def test_neapolitan_major_scale_over_octave():
    assert scale_comparator(NeapolitanMajorScale(Sounds.G),
                            {Sounds.G, Sounds.A.flat(), Sounds.B.flat(),
                             Sounds.C, Sounds.D, Sounds.E, Sounds.FIS
                             })


def test_octatonic_half_whole_scale():
    assert scale_comparator(OctatonicHalfWholeScale(Sounds.C),
                            {Sounds.C, Sounds.D.flat(), Sounds.E.flat(),
                             Sounds.E, Sounds.G.flat(), Sounds.G, Sounds.A,
                             Sounds.B.flat()
                             })


def test_octatonic_half_whole_scale_over_octave():
    assert scale_comparator(OctatonicHalfWholeScale(Sounds.G),
                            {Sounds.G, Sounds.A.flat(), Sounds.B.flat(),
                             Sounds.B, Sounds.D.flat(), Sounds.D, Sounds.E,
                             Sounds.F
                             })
