from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class HungarianMinorScale(Scale):
    """The Hungarian Gypsy Scale or the Hungarian Minor Scale 
    (sometimes only referred to as Hungarian Scale) is commonly 
    used in Indian classical music and, of course, Hungarian music. 
    The scale has also been used in rock and classical music. Using 
    the Hungarian scales will give your music an exotic touch.

    :link: https://www.pianoscales.org/hungarian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of hungarian minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HungarianMinorScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE
        ])


class HungarianMajorScale(Scale):
    """HungarianMajorScale

    :link: https://www.pianoscales.org/hungarian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of hungarian major scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HungarianMajorScale, self).__init__(key, [
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE
        ])
