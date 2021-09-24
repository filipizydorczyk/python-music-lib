from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class SpanishGypsyScale(Scale):
    """The Spanish Gypsy Scale is a common name for the 
    Phrygian Dominant Scale (a.k.a. Spanish Phrygian, 
    Spanish Major and, less often, Freygish or Ahava 
    Rabboh Scale, which is Hebrew for the Jewish Scale). 
    The notes in this scale are the same as for the Harmonic 
    Minor Scale, but with a different order – the A Harmonic 
    Minor, for example, is relative to the E Spanish Gypsy. 

    :link: https://www.pianoscales.org/spanish-gypsy.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of Spanish Gypsy Scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(SpanishGypsyScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
