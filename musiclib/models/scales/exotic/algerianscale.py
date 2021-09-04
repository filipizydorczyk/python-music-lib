from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class AlgerianScales(Scale):
    """The Algerian Scale has eight notes and the easiest way to memorize 
    them are by the intervals. The first thing that you should give 
    attention to in the Algerian scales is the three semi-steps that 
    follow in sequence from note four to seven. In total, the scale has 
    four halftones (see “Formula” below). 

    :link: https://www.pianoscales.org/algerian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Algerian scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(AlgerianScales, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
        ])
