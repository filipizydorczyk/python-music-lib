from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class NeapolitanMinorScale(Scale):
    """The Neapolitan scales originates from the city of 
    Naples and opera composers during the 18th century 
    such as Domenico Scarlatti and Domenico Cimarosa.
    There are both a minor and a major Neapolitan Scale. 
    The Minor Neapolitan can be seen as a Harmonic Minor 
    with a flat second note

    :link: https://www.pianoscales.org/neapolitan.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of whole Neapolitan minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(NeapolitanMinorScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
        ])


class NeapolitanMajorScale(Scale):
    """The Neapolitan scales originates from the city of 
    Naples and opera composers during the 18th century 
    such as Domenico Scarlatti and Domenico Cimarosa.
    There are both a minor and a major Neapolitan Scale. 
    Major Neapolitan can be seen as a Melodic Minor with 
    a flat second note

    :link: https://www.pianoscales.org/neapolitan.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of whole Neapolitan major scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(NeapolitanMajorScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
        ])
