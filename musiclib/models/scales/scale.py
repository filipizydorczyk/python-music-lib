from typing import Set, List
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class Scale:
    """This class contains set of sounds in scale for given key.
    """

    def __init__(self, key: Sounds, intervals: List[Intervals]) -> None:
        """creates instance of scale for given key built with given intervals

        :param key: key of scale
        :type key: Sounds
        """
        self.__sounds = set([key])

        current_note = key
        for interval in intervals:
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
