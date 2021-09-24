from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class YoScale(Scale):
    """This is one of the most common Japanese scales, 
    another one is in sen. The Yo Scale contains five 
    notes (it is almost similar to the Major Pentatonic 
    Scale), and is often used in Japanese folk music. 
    One way to learn this scale is to look at it as a 
    Major with the third and seventh degrees absent.

    :link: https://www.pianoscales.org/yo.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Yo Scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(YoScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
        ])
