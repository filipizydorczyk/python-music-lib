from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class MinorPentatonicScale(Scale):
    """Compared to the Natural Minor, the Minor Pentatonic omits 
    the half-note step intervals (2 and b6). Here are pictures 
    and notes of the Minor Pentatonic scales. These scales are 
    very common in many styles, but not least in pop and rock 
    music. See also Major Pentatonic Scales.

    :link: https://www.pianoscales.org/pentatonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(MinorPentatonicScale, self).__init__(key, [
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
        ])
