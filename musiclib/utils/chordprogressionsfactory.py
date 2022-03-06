from typing import Union
from typing import List

from musiclib.models.chord import Chord
from musiclib.models.scales.scale import Scale
from musiclib.models.chordprogression import ChordProgression
from musiclib.types.chordprogressions import ChordProgressions

def create(scale: Scale, progression: Union[str, ChordProgressions]) -> ChordProgression:
    return ChordProgression(scale, progression)

def create_progression_list(scale: Scale, progression: Union[str, ChordProgressions]) -> List[Chord]:
    return ChordProgression(scale, progression).get_chords_list()