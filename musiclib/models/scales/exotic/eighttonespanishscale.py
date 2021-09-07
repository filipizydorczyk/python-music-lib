from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class EightToneSpanishScale(Scale):
    """The Spanish Eight Tone Scale has its heritage from 
    the medieval period. It shares aspects with the Jewish 
    eight-tone scales and is common in Jewish music. These 
    scales are also Flamenco sounding, and therefore more 
    common among guitar players than piano players. 

    :link: https://www.pianoscales.org/eight-tone-spanish.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of eight tone spanish scale scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(EightToneSpanishScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE
        ])
