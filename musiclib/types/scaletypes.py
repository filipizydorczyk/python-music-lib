from __future__ import annotations
from enum import IntEnum, unique


@unique
class ScaleTypes(IntEnum):
    """We can categorize scales based on number of notes.

    :param IntEnum: numer of notes in scale
    :type IntEnum: int
    :lint: https://en.wikipedia.org/wiki/Scale_(music)
    """

    CHROMATIC = 12,
    NONATONIC = 9,
    OCTATONIC = 8,
    HEPTATONIC = 7,
    HEXATONIC = 6,
    PENTATONIC = 5,
    TETRATONIC = 4,
    TRITONIC = 3,
    DITONIC = 2,
