from enum import Enum, auto


class ChordProgressions(Enum):
    """This enum contains diffrent known chord progressions. 
    U can use them to create chord progression but it is also 
    possible to create one from string :class:`~musiclib.models.chordprogression.ChordProgression`
    """
    I_V_vi_IV = "I-V-vi-IV"
