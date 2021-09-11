from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class IwatoScale(Scale):
    """Iwato is the name of a Japanese Scale. It includes five notes 
    (which makes it to a pentatonic scale type), characterized by two 
    small and two big intervals. 

    :link: https://www.pianoscales.org/iwato.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of iwato scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(IwatoScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MAJOR_THIRD,
            Intervals.WHOLE_TONE,
        ])
