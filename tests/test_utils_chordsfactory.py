import pytest
from .context import create_major_chord, Pitch, Sounds, create, create_minor_chord, Chords


def test_create_major_chords():
    p = Pitch(Sounds.C, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.C
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.G

    p = Pitch(Sounds.CIS, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS

    p = Pitch(Sounds.D, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.A

    p = Pitch(Sounds.DIS, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.E, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.B

    p = Pitch(Sounds.F, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.F
    assert chord.get_pitches()[1].get_sound() == Sounds.A
    assert chord.get_pitches()[2].get_sound() == Sounds.C

    p = Pitch(Sounds.FIS, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.FIS
    assert chord.get_pitches()[1].get_sound() == Sounds.AIS
    assert chord.get_pitches()[2].get_sound() == Sounds.CIS

    p = Pitch(Sounds.G, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.G
    assert chord.get_pitches()[1].get_sound() == Sounds.B
    assert chord.get_pitches()[2].get_sound() == Sounds.D

    p = Pitch(Sounds.GIS, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.GIS
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS

    p = Pitch(Sounds.A, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.E

    p = Pitch(Sounds.AIS, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.AIS
    assert chord.get_pitches()[1].get_sound() == Sounds.D
    assert chord.get_pitches()[2].get_sound() == Sounds.F

    p = Pitch(Sounds.B, 4)
    chord = create_major_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.B
    assert chord.get_pitches()[1].get_sound() == Sounds.DIS
    assert chord.get_pitches()[2].get_sound() == Sounds.FIS


def test_create_minor_chords():
    p = Pitch(Sounds.C, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.C
    assert chord.get_pitches()[1].get_sound() == Sounds.DIS
    assert chord.get_pitches()[2].get_sound() == Sounds.G

    p = Pitch(Sounds.CIS, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS

    p = Pitch(Sounds.D, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.A

    p = Pitch(Sounds.DIS, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.E, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.B

    p = Pitch(Sounds.F, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.F
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.C

    p = Pitch(Sounds.FIS, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.FIS
    assert chord.get_pitches()[1].get_sound() == Sounds.A
    assert chord.get_pitches()[2].get_sound() == Sounds.CIS

    p = Pitch(Sounds.G, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.G
    assert chord.get_pitches()[1].get_sound() == Sounds.AIS
    assert chord.get_pitches()[2].get_sound() == Sounds.D

    p = Pitch(Sounds.GIS, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.GIS
    assert chord.get_pitches()[1].get_sound() == Sounds.B
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS

    p = Pitch(Sounds.A, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.E

    p = Pitch(Sounds.AIS, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.AIS
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.F

    p = Pitch(Sounds.B, 4)
    chord = create_minor_chord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.B
    assert chord.get_pitches()[1].get_sound() == Sounds.D
    assert chord.get_pitches()[2].get_sound() == Sounds.FIS


def test_create_minor_7_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.MINOR_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS
    assert chord.get_pitches()[3].get_sound() == Sounds.B

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.MINOR_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.A
    assert chord.get_pitches()[3].get_sound() == Sounds.C


def test_create_major_7_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.MAJOR_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS
    assert chord.get_pitches()[3].get_sound() == Sounds.C

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.MAJOR_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.A
    assert chord.get_pitches()[3].get_sound() == Sounds.CIS

    p = Pitch(Sounds.DIS, 5)
    chord = create(p, Chords.MAJOR_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS
    assert chord.get_pitches()[3].get_sound() == Sounds.D

    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.MAJ7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS
    assert chord.get_pitches()[3].get_sound() == Sounds.C

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.MAJ7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.A
    assert chord.get_pitches()[3].get_sound() == Sounds.CIS

    p = Pitch(Sounds.DIS, 5)
    chord = create(p, Chords.MAJ7)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS
    assert chord.get_pitches()[3].get_sound() == Sounds.D


def test_create_dominant_7_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.DOMINANT_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS
    assert chord.get_pitches()[3].get_sound() == Sounds.B

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.DOMINANT_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.A
    assert chord.get_pitches()[3].get_sound() == Sounds.C

    p = Pitch(Sounds.DIS, 5)
    chord = create(p, Chords.DOMINANT_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS
    assert chord.get_pitches()[3].get_sound() == Sounds.CIS


def test_create_diminished_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.DIMINISHED)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.G

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.DIMINISHED)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS

    p = Pitch(Sounds.E, 5)
    chord = create(p, Chords.DIMINISHED)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.A, 2)
    chord = create(p, Chords.DIMINISHED)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS


def test_create_diminished_7_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.DIMINISHED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.G
    assert chord.get_pitches()[3].get_sound() == Sounds.AIS

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.DIMINISHED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS
    assert chord.get_pitches()[3].get_sound() == Sounds.B

    p = Pitch(Sounds.E, 5)
    chord = create(p, Chords.DIMINISHED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS
    assert chord.get_pitches()[3].get_sound() == Sounds.CIS

    p = Pitch(Sounds.A, 2)
    chord = create(p, Chords.DIMINISHED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS
    assert chord.get_pitches()[3].get_sound() == Sounds.FIS


def test_create_augmented_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.AUGMENTED)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.A

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.AUGMENTED)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.E, 5)
    chord = create(p, Chords.AUGMENTED)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.C

    p = Pitch(Sounds.A, 2)
    chord = create(p, Chords.AUGMENTED)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.F


def test_create_augmented_7_chords():
    p = Pitch(Sounds.CIS, 4)
    chord = create(p, Chords.AUGMENTED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.A
    assert chord.get_pitches()[3].get_sound() == Sounds.B

    p = Pitch(Sounds.D, 3)
    chord = create(p, Chords.AUGMENTED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS
    assert chord.get_pitches()[3].get_sound() == Sounds.C

    p = Pitch(Sounds.E, 5)
    chord = create(p, Chords.AUGMENTED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.C
    assert chord.get_pitches()[3].get_sound() == Sounds.D

    p = Pitch(Sounds.A, 2)
    chord = create(p, Chords.AUGMENTED_7)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.F
    assert chord.get_pitches()[3].get_sound() == Sounds.G
