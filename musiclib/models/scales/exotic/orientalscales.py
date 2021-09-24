from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class OrientalScale(Scale):
    """The Oriental Scale has a Chinese origin (not to 
    be confused with the Chinese Scale, thought), and 
    is an octatonic scale (a scale consisting of eight 
    notes). A feature to observe then you try to learn 
    the scale is that it is characterized by groups of 
    semi-note intervals (see scale formula below). 

    :link: https://www.pianoscales.org/oriental.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Oriental Scales for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(OrientalScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])
