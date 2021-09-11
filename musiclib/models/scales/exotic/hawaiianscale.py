from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class HawaiianScale(Scale):
    """The Hawaiian Scale consists of seven notes. The intervals 
    include whole steps throughout the scale except one half steps, 
    and additionally a half step to the note one octave up.

    Notice what this scale is identical with ascending version of the 
    Melodic Minor Scale.

    :link: https://www.pianoscales.org/hawaiian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Hawaiian tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HawaiianScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE
        ])
