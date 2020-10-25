from abc import ABCMeta, abstractmethod
from musiclib.models.chords.chord import Chord
from musiclib.types.chords import Chords
from musiclib.models.note import Note


class MajorChord(Chord):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def add_note(self, note: Note) -> Chord:
        pass

    @abstractmethod
    def get_chord_type(self) -> Chords:
        return Chords.MAJOR
