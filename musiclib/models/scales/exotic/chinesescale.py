from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class ChineseScale(Scale):
    """As implied by its name, this scale is suitable for playing Chinese
    music (see also the Oriental Scale). The Chinese scales are sometimes 
    used in jazz improvisation.

    The Chinese Scale has a quite uncommon feature in the two quadra-steps: 
    first to second note and fourth to fifth note. Another peculiar detail 
    is that a harmony note is added to every single note in the scale (see 
    below).

    :link: https://www.pianoscales.org/chinese.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of balinese tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(ChineseScale, self).__init__(key, [
            Intervals.MAJOR_THIRD,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD,
            Intervals.HALF_TONE,
        ])
