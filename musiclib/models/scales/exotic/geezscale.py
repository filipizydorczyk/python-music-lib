from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.notesorder import NotesOrder
from musiclib.types.sounds import Sounds


class GeezScale(Scale):
    """The Geez Scale (also known as Ezel Scale) is an Ethiopian scale, 
    and in its form identical to the Aeolian Scale. Worth mentioning is 
    that another Ethiopian scale, Ararai, has exactly the same notes as 
    the Major Scale.

    :link: https://www.pianoscales.org/ethiopian-geez.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of enigmatic geez scale scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(GeezScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])
