from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class AugmentedScale(Scale):
    """The Augmented Scale (a.k.a. Symmetrical Augmented Scale) consists 
    of six notes and therefore belongs to the category of hexatonic scales. 
    The name of the scale is based on the fact that it is built upon two 
    augmented chords. In the C Augmented Scale this would be 
    C - E - G# (Caug) and Eb - G - B (Ebaug). 

    This scale should not be confused with Whole Tone Scale or 
    Lydian Augmented with the semi-notes pattern 2 - 2 - 2 - 2 - 1 - 2 - 1.

    :link: https://www.pianoscales.org/augmented.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of augmented tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(AugmentedScale, self).__init__(key, [
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
        ])
