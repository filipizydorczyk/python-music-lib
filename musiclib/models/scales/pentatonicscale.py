from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class MinorPentatonicScale(Scale):
    """Compared to the Natural Minor, the Minor Pentatonic omits 
    the half-note step intervals (2 and b6). Here are pictures 
    and notes of the Minor Pentatonic scales. These scales are 
    very common in many styles, but not least in pop and rock 
    music. See also Major Pentatonic Scales. You can also reffer
    to this scale as PentatonicScale. Since this is slightly more
    often use (in scope of pentatonic scales) this lib consider
    MinorPentatonicScale as "default pentatnoic scale" xD

    :link: https://www.pianoscales.org/pentatonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of minor pentatonic scale for given key

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


class MajorPentatonicScale(Scale):
    """This five-note scale is similar to the Major Scale, 
    but without the 4th and 7th degrees. Major Pentatonic scales 
    are especially common in traditional folk music, country and 
    gospel. Here are pictures and notes of the Major Pentatonic 
    scale.

    :link: https://www.pianoscales.org/pentatonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of major pentatonic scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(MajorPentatonicScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
        ])
