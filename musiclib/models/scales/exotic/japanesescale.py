from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class JapaneseScale(Scale):
    """This is one of the most common among Japanese scales 
    (there are other scales sometimes called simply with 
    names such as "Japanese 1" and "Japanese 2"), and often 
    referred to as the Japanese Scale. It is also referred 
    to as "in sen scale" (not to be confused with the "in 
    scale"). 

    :link: https://www.pianoscales.org/japanese-in-sen.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Japanese scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(JapaneseScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.DIMINISHED_FOURTH,
            Intervals.WHOLE_TONE,
            Intervals.AUGMENTED_SECOND,
            Intervals.WHOLE_TONE,
        ])
