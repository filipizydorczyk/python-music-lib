from .note import Note


class Sequencer:

    def __init__(self, seqences: list):
        self.__seqences = seqences

    def performe_sequence(self, start_note: Note, steps: int = len(self.__seqences)) -> list:
        return None
