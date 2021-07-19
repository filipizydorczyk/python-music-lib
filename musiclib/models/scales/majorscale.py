from typing import Set
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class MajorScale:
    """This class contains set of sounds in major scale for given key.
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of major scale for given key

        :param key: key of scale
        :type key: Sounds
        """
        self.__sounds = set([key])

        current_note = key
        for interval in [
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE
        ]:
            current_note = current_note.add(interval)
            self.__sounds.add(current_note)

    def get_scale_sounds(self) -> Set[Sounds]:
        """returns set of sounds in created scale

        :return: set of sounds in created scale. Returned
        value is copy of class field so that u couldn't
        make change in Scale. If u want to pursue changes in
        scale, assign returned set to variable and work on
        that variable. 
        :rtype: Set[Sounds]
        """
        return self.__sounds.copy()
