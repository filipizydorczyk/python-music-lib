from typing import Union
from typing import List

from musiclib.models.chord import Chord
from musiclib.models.scales.scale import Scale
from musiclib.models.chordprogression import ChordProgression
from musiclib.types.chordprogressions import ChordProgressions

def create_chordprogression(scale: Scale, progression: Union[str, ChordProgressions]) -> ChordProgression:
    """creates instance of chord progression

    :param scale: scale that chord progression should be created for
    :type scale: Scale
    :param progression: string or enum of progression to be created
    :type progression: Union[str, ChordProgressions]
    :return: instance of chord progression containing created chords
    :rtype: ChordProgression
    """
    return ChordProgression(scale, progression)

def create_chordprogression_list(scale: Scale, progression: Union[str, ChordProgressions]) -> List[Chord]:
    """creates list of chords for given scale and progression

    :param scale: scale that chord progression should be created for
    :type scale: Scale
    :param progression: string or enum of progression to be created
    :type progression: Union[str, ChordProgressions]
    :return: list of chords
    :rtype: List[Chord]
    """
    return ChordProgression(scale, progression).get_chords_list()