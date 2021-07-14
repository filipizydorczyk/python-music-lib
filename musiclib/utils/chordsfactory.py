from musiclib.types.intervals import Intervals
from musiclib.models.chord import Chord
from musiclib.models.pitch import Pitch
from musiclib.types.chords import Chords
from musiclib.collections.pitcheslist import PitchesList


chord_dictionary = {
    Chords.MAJOR: [Intervals.MAJOR_THIRD, Intervals.PERFECT_FIFTH],
    Chords.MINOR: [Intervals.MINOR_THIRD, Intervals.PERFECT_FIFTH]

}


def createMajorChord(pitch: Pitch) -> Chord:
    """create major chord of given pitch

    :param pitch: chord root pitch
    :type pitch: Pitch
    :return: major chord in one octave
    :rtype: Chord
    """
    plist = PitchesList()
    plist.append(pitch)
    for inter in chord_dictionary[Chords.MAJOR]:
        plist.append(pitch.add(inter))

    return Chord(plist, 1.0)


def createMinorChord(pitch: Pitch) -> Chord:
    """create minor chord of given pitch

    :param pitch: chord root pitch
    :type pitch: Pitch
    :return: minor chord in one octave
    :rtype: Chord
    """
    plist = PitchesList()
    plist.append(pitch)
    for inter in chord_dictionary[Chords.MINOR]:
        plist.append(pitch.add(inter))

    return Chord(plist, 1.0)


def create7thChord() -> Chord:
    pass


def create(pitch: Pitch, chord_type: Chords) -> Chord:
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
