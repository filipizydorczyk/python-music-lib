from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class WholeToneScale(Scale):
    """The Whole Tone Scale (a.k.a. the Augmented Scale) is, as the name implies, 
    built from notes with intervals of a whole note. This is a so-called symmetrical 
    scale, meaning that the interval is the same throughout the scale. A whole tone 
    is the same as two steps on the keyboard – a half tone is consequently one step.

    :link: https://www.pianoscales.org/whole-tone.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(WholeToneScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
