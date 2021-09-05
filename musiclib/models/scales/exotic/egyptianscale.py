from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class EgyptianScale(Scale):
    """The Egyptian Scale is built by five notes, making it a pentatonic scale type. 
    This scale can be referred to different names. The scales displayed in diagrams 
    below can be called Egyptian, but you may witness scales built differently also 
    being called Egyptian scales.

    :link: https://www.pianoscales.org/egyptian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of dominant diminished scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(EgyptianScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
        ])
