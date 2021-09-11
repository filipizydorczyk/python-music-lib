from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class HirajoshiScale(Scale):
    """Hirajoshi is the name of a Japanese Scale that was originally used 
    in shamisen music. The word Hirajoshi is more correctly written with 
    a macron: Hirajōshi.

    This is a pentatonic scale (it uses five tones), characterized by two 
    half steps and two quadra-steps. You may find the Hirajoshi Scale in other 
    patterns, but the version presented here is probably the most common.

    :link: https://www.pianoscales.org/hirajoshi.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Hirajoshi scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HirajoshiScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD
        ])
