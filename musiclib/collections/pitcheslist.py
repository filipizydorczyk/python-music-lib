from musiclib.types.intervals import Intervals


class PitchesList(list):

    def append(self, element_to_add) -> None:
        adding_element = element_to_add
        if type(element_to_add) is Intervals:
            notes = len(self)
            if(notes > 0):
                last_element = self[notes-1]
            adding_element = ""
        list.append(adding_element)
