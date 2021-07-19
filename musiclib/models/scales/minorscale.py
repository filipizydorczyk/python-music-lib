from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class MinorScale(Scale):
    """This class contains set of sounds in minor scale for given key.
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(MinorScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_STEP,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_STEP,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
