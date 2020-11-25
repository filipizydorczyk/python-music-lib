from typing import Union

from musiclib.types.intervals import Intervals
from musiclib.models.pitch import Pitch


class PitchesList(list):
    """collection of pitches. It extends doing of default list. All method are available, if working of one is modified there it is documentated.
    """

    def append(self, element_to_add: Union[Pitch, Intervals]) -> None:
        """appends Pitch model to list

        :param element_to_add: u can add new Pitch to the list by providing new Pitch instance or Interval. Iterval will add new Pitch increased by given interval in relation to last inserted Pitch. Will be no added new element if length of collection is 0 and we are tring to add interval.
        :type element_to_add: Union[Pitch, Intervals]
        """
        adding_element = element_to_add
        if type(element_to_add) is Intervals:
            notes = len(self)
            if(notes > 0):
                last_element = self[notes-1]
                adding_element = last_element.add(element_to_add)
            else:
                return

        super().append(adding_element)
