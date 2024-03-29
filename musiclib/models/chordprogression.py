from typing import Union
from typing import List
from typing import Mapping
from typing import Tuple

from musiclib.types.chords import Chords
from musiclib.models.chord import Chord
from musiclib.models.pitch import Pitch
from musiclib.models.scales.scale import Scale
from musiclib.types.chordprogressions import ChordProgressions
from musiclib.utils.chordsfactory import create_chord

number_to_chord_dictionary: Mapping[str, Tuple[int, Chords]] = {
    "I": (1, Chords.MAJOR),
    "Im7": (1, Chords.MINOR_7),
    "i": (1, Chords.MINOR),
    "II": (2, Chords.MAJOR),
    "IIm7": (2, Chords.MINOR_7),
    "ii": (2, Chords.MINOR),
    "III": (3, Chords.MAJOR),
    "IIIm7": (4, Chords.MINOR_7),
    "iii": (3, Chords.MINOR),
    "IV": (4, Chords.MAJOR),
    "IVm7": (4, Chords.MINOR_7),
    "iv": (4, Chords.MINOR),
    "V": (5, Chords.MAJOR),
    "Vm7": (5, Chords.MINOR_7),
    "v": (5, Chords.MINOR),
    "VI": (6, Chords.MAJOR),
    "VIm7": (6, Chords.MINOR_7),
    "vi": (6, Chords.MINOR),
}


class ChordProgressionStringFormat(Exception):
    pass


class ChordProgression:
    """This model keeps information about chord progression and usefull related methods.

    For this class correctly formated progression string is crucial. Every string 
    contains list of chords seperated by `-`. Every chord is described by roman numerals 
    (I,II,IV etc...) which describe wich note of the scale is root of this chord. Chord 
    can be uppercased or lowercased. Uppercased are major chords and lowercased are minor 
    chords. For now it's really basic implementation and only these two types are 
    implemented in future there will be more chords available. 
    """

    def __init__(self, scale: Scale, progression: Union[str, ChordProgressions]):
        """Creates new instance of chord progression.

        :param scale: scale that chord preogression is suppose to be created for
        :type scale: Scale
        :param progression: U can use one of predefined 
            progressions in :enum:`~musiclib.types.chordprogressions.ChordProgressions` 
            or u can define own progression by passing string. String should be formatted 
            in correct way otherwise error will be raised. Example of valid progression string
            is "I-V-vi-IV". More explenation above
        :type progression: Union[str, ChordProgressions]
        """
        # TODO: Custom colletction for keeping chords
        self.__chords: List[Chord] = []
        progression_to_split: str = progression

        if type(progression) is ChordProgressions:
            progression_to_split = progression.value

        for chord in progression_to_split.split("-"):
            mapping = None
            try:
                mapping = number_to_chord_dictionary[chord]
            except:
                raise ChordProgressionStringFormat(
                    "Chord not found. Make sure string is formated correctly")
            self.__chords.append(
                create_chord(
                    Pitch(scale.get_scale_sounds_list()[mapping[0] - 1], 1),
                    mapping[1]
                )
            )

    def get_chords_list(self) -> List[Chord]:
        """get list of chords for given progression

        :return: list of chords
        :rtype: List[Chord]
        """
        return self.__chords
