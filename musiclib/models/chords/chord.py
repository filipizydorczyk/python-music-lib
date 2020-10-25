from __future__ import annotations
from abc import ABCMeta, abstractmethod
from musiclib.models.note import Note
from musiclib.types.chords import Chords


class Chord:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__notes = []

    def get_notes(self):
        return self.__notes

    @abstractmethod
    def add_note(self, note: Note) -> Chord:
        pass

    @abstractmethod
    def get_chord_type(self) -> Chords:
        pass
