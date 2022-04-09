from enum import Enum


class ChordProgressions(Enum):
    """This enum contains diffrent known chord progressions. 
    U can use them to create chord progression but it is also 
    possible to create one from string :class:`~musiclib.models.chordprogression.ChordProgression`
    """
    I_V_vi_IV = "I-V-vi-IV"
    Im7_Vm7_IVm7_IVm7 = "Im7-Vm7-IVm7-IVm7"
    Im7_Vm7_IVm7_Im7 = "Im7-Vm7-IVm7-Im7"
