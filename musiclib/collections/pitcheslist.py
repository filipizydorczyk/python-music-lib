from musiclib.types.intervals import Intervals


class PitchesList(list):

    def append(self, element_to_add) -> None:
        adding_element = element_to_add
        if type(element_to_add) is Intervals:
            adding_element = ""
        self.append(element_to_add)
