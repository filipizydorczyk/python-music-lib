from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class OctatonicHalfWholeScale(Scale):
    """The Octatonic Scale consists, as the name implies, 
    of eight notes. (An octatonic scale is also used as a 
    term to describe a scale with eight notes in it.) The 
    scale alternates half and whole steps and there are 
    two different versions with intervals ordered contrarily. 

    :link: https://www.pianoscales.org/octatonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of whole Octatonic (Half Whole) Scales for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(OctatonicHalfWholeScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
        ])


class OctatonicWholeHalfScale(Scale):
    """The Octatonic Scale consists, as the name implies, 
    of eight notes. (An octatonic scale is also used as a 
    term to describe a scale with eight notes in it.) The 
    scale alternates half and whole steps and there are 
    two different versions with intervals ordered contrarily. 

    :link: https://www.pianoscales.org/octatonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Octatonic (Whole Half) Scales for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(OctatonicWholeHalfScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
        ])
