from musiclib.types.intervals import Intervals
from musiclib.models.chord import Chord
from musiclib.models.pitch import Pitch
from musiclib.types.chords import Chords
from musiclib.collections.pitcheslist import PitchesList


def createMajorChord(pitch: Pitch) -> Chord:
    plist = PitchesList()
    plist.append(pitch)
    plist.append(pitch.add(Intervals.MAJOR_THIRD))
    plist.append(pitch.add(Intervals.PERFECT_FIFTH))
    return Chord(plist, 1.0)


def createMinorChord() -> Chord:
    pass


def create7thChord() -> Chord:
    pass


def create(chord_type: Chords) -> Chord:
    pass
