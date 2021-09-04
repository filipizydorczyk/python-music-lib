from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class ByzantineScale(Scale):
    """The Byzantine Scale, also known as the Double Harmonic Scale, 
    has a configuration that produces an exotic sound. What characterizes 
    this scale are the whole and a half semi-step intervals between the 
    second and third and the sixth and seventh notes. 

    The easiest way to learn the Byzantine scales is probably by comparing 
    them with the Major Scales. The only differences are the second and sixth 
    notes which both are lowered. 

    :link: https://www.pianoscales.org/byzantine.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of balinese tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(ByzantineScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
        ])
