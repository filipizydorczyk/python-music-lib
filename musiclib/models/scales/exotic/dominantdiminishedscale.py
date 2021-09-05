from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class DominantDiminishedScale(Scale):
    """The Dominant Diminished Scale consists of eight notes, 
    and therefore belongs to the category of octatonic scales. 
    It is also a so-called symmetrical scale since the intervals 
    are consistent. The half tone, whole tone formula is consistent 
    throughout the scale, for which reason it is sometimes called 
    the Half-tone/Whole-tone Scale.

    The Dominant Diminished Scale is also referred to as the Diminished 
    Blues (therefore u can reffer to it also as 
    musiclib.models.scales.exotic.DiminishedBluesScale) and it shares 
    many notes with the Pentatonic Blues scales.

    :link: https://www.pianoscales.org/dominant-diminished.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of dominant diminished scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(DominantDiminishedScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])
