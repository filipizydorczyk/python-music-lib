from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class RomanianMinorScale(Scale):
    """The Romanian Scale brings a beautiful melancholic 
    sound of the Romanian folk music with a touch of gypsy. 
    See pictures below of all Romanian Minor scales for 
    piano.

    :link: https://www.pianoscales.org/romanian-minor.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Romanian Minor Scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(RomanianMinorScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])
