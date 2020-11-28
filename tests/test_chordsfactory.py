import pytest
from .context import createMajorChord, Pitch, Sounds, create, createMinorChord, Chords


def test_create_major_chords():
    p = Pitch(Sounds.C, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.C
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.G

    p = Pitch(Sounds.CIS, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS

    p = Pitch(Sounds.D, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.A

    p = Pitch(Sounds.DIS, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.E, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.B

    p = Pitch(Sounds.F, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.F
    assert chord.get_pitches()[1].get_sound() == Sounds.A
    assert chord.get_pitches()[2].get_sound() == Sounds.C

    p = Pitch(Sounds.FIS, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.FIS
    assert chord.get_pitches()[1].get_sound() == Sounds.AIS
    assert chord.get_pitches()[2].get_sound() == Sounds.CIS

    p = Pitch(Sounds.G, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.G
    assert chord.get_pitches()[1].get_sound() == Sounds.B
    assert chord.get_pitches()[2].get_sound() == Sounds.D

    p = Pitch(Sounds.GIS, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.GIS
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS

    p = Pitch(Sounds.A, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.E

    p = Pitch(Sounds.AIS, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.AIS
    assert chord.get_pitches()[1].get_sound() == Sounds.D
    assert chord.get_pitches()[2].get_sound() == Sounds.F

    p = Pitch(Sounds.B, 4)
    chord = createMajorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.B
    assert chord.get_pitches()[1].get_sound() == Sounds.DIS
    assert chord.get_pitches()[2].get_sound() == Sounds.FIS


def test_create_minor_chords():
    p = Pitch(Sounds.C, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.C
    assert chord.get_pitches()[1].get_sound() == Sounds.DIS
    assert chord.get_pitches()[2].get_sound() == Sounds.G

    p = Pitch(Sounds.CIS, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.CIS
    assert chord.get_pitches()[1].get_sound() == Sounds.E
    assert chord.get_pitches()[2].get_sound() == Sounds.GIS

    p = Pitch(Sounds.D, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.D
    assert chord.get_pitches()[1].get_sound() == Sounds.F
    assert chord.get_pitches()[2].get_sound() == Sounds.A

    p = Pitch(Sounds.DIS, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.DIS
    assert chord.get_pitches()[1].get_sound() == Sounds.FIS
    assert chord.get_pitches()[2].get_sound() == Sounds.AIS

    p = Pitch(Sounds.E, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.E
    assert chord.get_pitches()[1].get_sound() == Sounds.G
    assert chord.get_pitches()[2].get_sound() == Sounds.B

    p = Pitch(Sounds.F, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.F
    assert chord.get_pitches()[1].get_sound() == Sounds.GIS
    assert chord.get_pitches()[2].get_sound() == Sounds.C

    p = Pitch(Sounds.FIS, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.FIS
    assert chord.get_pitches()[1].get_sound() == Sounds.A
    assert chord.get_pitches()[2].get_sound() == Sounds.CIS

    p = Pitch(Sounds.G, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.G
    assert chord.get_pitches()[1].get_sound() == Sounds.AIS
    assert chord.get_pitches()[2].get_sound() == Sounds.D

    p = Pitch(Sounds.GIS, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.GIS
    assert chord.get_pitches()[1].get_sound() == Sounds.B
    assert chord.get_pitches()[2].get_sound() == Sounds.DIS

    p = Pitch(Sounds.A, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.A
    assert chord.get_pitches()[1].get_sound() == Sounds.C
    assert chord.get_pitches()[2].get_sound() == Sounds.E

    p = Pitch(Sounds.AIS, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.AIS
    assert chord.get_pitches()[1].get_sound() == Sounds.CIS
    assert chord.get_pitches()[2].get_sound() == Sounds.F

    p = Pitch(Sounds.B, 4)
    chord = createMinorChord(p)
    assert chord.get_pitches()[0].get_sound() == Sounds.B
    assert chord.get_pitches()[1].get_sound() == Sounds.D
    assert chord.get_pitches()[2].get_sound() == Sounds.FIS


def test_create_chords_by_type():
    p = Pitch(Sounds.B, 4)
    chord = createMinorChord(p)
    by_type_chord = create(p, Chords.MINOR)

    assert chord.get_pitches()[0] == by_type_chord.get_pitches()[0]
    assert chord.get_pitches()[1] == by_type_chord.get_pitches()[1]
    assert chord.get_pitches()[2] == by_type_chord.get_pitches()[2]

    p = Pitch(Sounds.B, 4)
    chord = createMajorChord(p)
    by_type_chord = create(p, Chords.MAJOR)

    assert chord.get_pitches()[0] == by_type_chord.get_pitches()[0]
    assert chord.get_pitches()[1] == by_type_chord.get_pitches()[1]
    assert chord.get_pitches()[2] == by_type_chord.get_pitches()[2]
