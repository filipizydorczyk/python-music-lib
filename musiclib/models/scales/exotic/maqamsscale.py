from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds
from enum import IntEnum


class Chords(IntEnum):
    HIJAZ_KAR_MAQAM = Sounds.C,
    SHAHNAZ = Sounds.D,
    MAQAM_MUSTAR = Sounds.E.flat(),
    MAQAM_JIHARKAH = Sounds.F,
    SHADD_ARABAN = Sounds.G,
    SUZIDIL = Sounds.A,
    AJAM_MAQAM = Sounds.B.flat()


class MaqamsScale(Scale):
    """The maqams (Arabic for position) can be called scales
     or modes and are common in music from the Middle East 
     and in Turkish Ottoman classical music ("Makam" can be 
     translated to scales or modes in Turkish). One of the 
     things that distinguish a maqam from a scale is that a 
     maqam sometimes uses quarter tones (a pitch between two 
     semi-notes, such as a tone between F# and G). 

     There are lots of maqams which are organized into several 
     groups and sometimes hard to grasp at the first moment. 
     The scale is Arabic maqam. The scales in different keys 
     also have specific names. Maqams often begins on C, D, 
     Eb (quarter-flat), F, G, A or Bb (quarter-flat). 

    :link: https://www.pianoscales.org/maqams.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Maqams scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(MaqamsScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
