from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class LydianDominantScale(Scale):
    """The scale differs from the regular Lydian Mode by including a 
    minor seventh, which is the reason for it being called “dominant” 
    (see Dominant scales). Since it includes the minor seventh, the 
    scale is suitable for playing over a dominant seventh chord and 
    especially the 7(#11) chord. The Lydian b7 can be seen as a mode 
    of the Melodic Minor Scale.

    :link: https://www.pianoscales.org/lydian-dominant.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Lydian Dominant scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(LydianDominantScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])
