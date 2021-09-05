from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class DiminishedScale(Scale):
    """The Diminished Scale is built upon two diminished seventh chords. 
    In the C Diminished Scale this would be C - Eb - Gb - A (Cdim7) and 
    D - F - Ab - B (Ddim7). This scale is primarily used in jazz music 
    and works well together with alternate seventh chords.

    The Diminished Scale is also referred to as the Whole-half Scale 
    since it is constructed by every second whole and half steps 
    (notice also that it is a symmetrical scale).

    :link: https://www.pianoscales.org/diminished.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of diminished tone scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(DiminishedScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
        ])
