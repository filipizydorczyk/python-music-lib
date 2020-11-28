from enum import IntEnum, unique


@unique
class ChordCategories(IntEnum):
    TRIADS = 0,
    SEVENTH = 1,
    EXTENDED_CHORDS = 2,
    OTHER_MAJOR_CHORDS = 3,
    SUSPENDED = 4,
    OMITTED = 5,
    ALTERATIONS = 6,
    ADDED = 7
