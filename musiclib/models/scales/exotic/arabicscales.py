from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class ArabicScales(Scale):
    """There are actually two different scales referred to as “Arabian”. 
    One is similar to the Major Locrian Scale and the other to the Diminished Scale. 
    The scales illustrated below in all keys belong to the former. They can easy be 
    memorized if compared to the Major Scale: the fifth, sixth and seventh is lowered 
    half a step and the rest of the notes are just the same as in the Major. 

    The scale is not officially named “Arabic Scale”, but since it is often used in 
    Arabic music it is adequate to call it so.

    :link: https://www.pianoscales.org/arabic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of arabic scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(ArabicScales, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
