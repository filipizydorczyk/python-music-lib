from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class HinduScale(Scale):
    """The Aeolian Dominant Scale is often referred to as the Hindu Scale, 
    and therefore suitable for playing Indian music. The scale includes a 
    minor seventh, which is the reason for it being called “dominant”.

    The Aeolian Dominant Scale is similar to the Aeolian mode except the 
    third note in the scale that is raised one semi-step. It can also be 
    compared to the Mixolydian mode, only the sixth note differs.

    :link: https://www.pianoscales.org/aeolian-dominant.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of hindu scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HinduScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE
        ])
