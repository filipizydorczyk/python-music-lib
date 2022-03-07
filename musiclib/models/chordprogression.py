from typing import Union
from typing import List
from typing import Mapping
from typing import Tuple

from musiclib.types.chords import Chords
from musiclib.models.chord import Chord
from musiclib.models.scales.scale import Scale
from musiclib.types.chordprogressions import ChordProgressions
from musiclib.utils.chordsfactory import create

number_to_chord_dictionary: Mapping[str,Tuple[int,Chords]] = {
    "I": (1, Chords.MAJOR),
    "i": (1,Chords.MINOR),
    "II": (2, Chords.MAJOR),
    "ii": (2,Chords.MINOR),
    "III": (3, Chords.MAJOR),
    "iii": (3,Chords.MINOR),
    "IV": (4, Chords.MAJOR),
    "iv": (4,Chords.MINOR),
    "V": (5, Chords.MAJOR),
    "v": (5,Chords.MINOR),
    "VI": (6, Chords.MAJOR),
    "vi": (6,Chords.MINOR),
}

class ChordProgressionStringFormat(Exception):
    pass


class ChordProgression:
    """This model keeps information about chord progression and usefull related methods.
    """
    def __init__(self, scale: Scale, progression: Union[str, ChordProgressions]):
        """Creates new instance of chord progression.

        :param scale: scale that chord preogression is suppose to be created for
        :type scale: Scale
        :param progression: U can use one of predefined 
            progressions in :enum:`~musiclib.types.chordprogressions.ChordProgressions` 
            or u can define own progression by passing string. String should be formatted 
            in correct way otherwise error will be raised. Example of valid progression string
            is "I-V-vi-IV".
        :type progression: Union[str, ChordProgressions]
        """
        # TODO: Custom colletction for keeping chords
        self.__chords: List[Chord] = []
        progression_to_split: str = progression

        if type(progression) is ChordProgressions:
            progression_to_split = progression.value

        print(progression_to_split)

        for chord in progression_to_split.split("-"):
            print(chord)
            mapping = None
            try:
                mapping = number_to_chord_dictionary[chord]
                print(mapping)
            except:
                raise ChordProgressionStringFormat("Chord not found. Make sure string is formated correctly")
            self.__chords.append(
                    create(
                        scale.get_scale_sounds_list()[mapping[0] - 1],
                        mapping[1]
                        )
                    )

    def get_chords_list(self) -> List[Chord]:
        return self.__chords