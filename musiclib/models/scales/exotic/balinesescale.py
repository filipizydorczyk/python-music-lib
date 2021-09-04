from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class BalineseScale(Scale):
    """The Balinese Scale (a.k.a. Balinese Pelog Scale) consists of five notes, 
    which makes it a pentatonic scale. The intervals include two half steps, 
    one whole step and two quadra-steps.

    :link: https://www.pianoscales.org/balinese.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of balinese tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(BalineseScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MAJOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD
        ])
