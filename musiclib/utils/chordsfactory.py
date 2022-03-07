from musiclib.types.intervals import Intervals
from musiclib.models.chord import Chord
from musiclib.models.pitch import Pitch
from musiclib.types.chords import Chords
from musiclib.collections.pitcheslist import PitchesList


chord_dictionary = {
    Chords.MAJOR: [Intervals.MAJOR_THIRD, Intervals.PERFECT_FIFTH],
    Chords.MAJOR_7: [Intervals.MAJOR_THIRD, Intervals.PERFECT_FIFTH, Intervals.MAJOR_SEVENTH],
    Chords.MAJ7: [Intervals.MAJOR_THIRD, Intervals.PERFECT_FIFTH, Intervals.MAJOR_SEVENTH],
    Chords.MINOR: [Intervals.MINOR_THIRD, Intervals.PERFECT_FIFTH],
    Chords.MINOR_7: [Intervals.MINOR_THIRD, Intervals.PERFECT_FIFTH, Intervals.MINOR_SEVENTH],
    Chords.DOMINANT_7: [Intervals.MAJOR_THIRD, Intervals.PERFECT_FIFTH, Intervals.MINOR_SEVENTH],
    Chords.DIMINISHED: [Intervals.MINOR_THIRD, Intervals.DIMINISHED_FIFTH],
    Chords.DIMINISHED_7: [Intervals.MINOR_THIRD,
                          Intervals.DIMINISHED_FIFTH, Intervals.DIMINISHED_SEVENTH],
    Chords.AUGMENTED: [Intervals.MAJOR_THIRD, Intervals.AUGMENTED_FIFTH],
    Chords.AUGMENTED_7: [Intervals.MAJOR_THIRD,
                         Intervals.AUGMENTED_FIFTH, Intervals.MINOR_SEVENTH],
}


def create_chord_major(pitch: Pitch) -> Chord:
    """create major chord of given pitch

    :param pitch: chord root pitch
    :type pitch: Pitch
    :return: major chord in one octave
    :rtype: Chord
    """
    return create_chord(pitch, Chords.MAJOR)


def create_minor_chord(pitch: Pitch) -> Chord:
    """create minor chord of given pitch

    :param pitch: chord root pitch
    :type pitch: Pitch
    :return: minor chord in one octave
    :rtype: Chord
    """
    return create_chord(pitch, Chords.MINOR)


def create_chord(pitch: Pitch, chord_type: Chords) -> Chord:
    """create chord of given pitch and type

    :param pitch: root pitch
    :type pitch: Pitch
    :param chord_type: type of chord we want to create (MAJOR, MINOR etc.)
    :type chord_type: Chords
    :return: created Chord instance or None if chord_type is not implemented or doesn't exist in package
    :rtype: Chord
    """
    plist = PitchesList()
    plist.append(pitch)
    for inter in chord_dictionary[chord_type]:
        plist.append(pitch.add(inter))

    return Chord(plist, 1.0)
