from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class SuperLocrianScale(Scale):
    """The Super Locrian, also known as the Dominant 
    Altered Scale, is built on the Locrian Mode and 
    is particularly used in modern jazz and fusion. 
    The scale is typically used together with altered 
    dominant seventh chords, such as 7b9 and 7#9. 
    Yet another name for this scale is Diminished 
    Whole Tone. The scale is also identical to 
    the seventh mode of the Melodic Minor 
    (e.g. G# Super Locrian is identical 
    to A Melodic Minor).

    :link: https://www.pianoscales.org/super-locrian.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Super Locrian Scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(SuperLocrianScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
