from .context import Note, NoteDurations, Sounds, printTestHeader

import unittest


class NoteTest(unittest.TestCase):

    """Basic test cases."""

    def create_instance_test(self):
        printTestHeader("Note Test", "create_instance_test")
        note = Note(Sounds.A, 3, NoteDurations.EIGHTH_NOTE)
        assert note.get_sound() == Sounds.A
        assert note.get_octave() == 3
        assert note.get_duration() == NoteDurations.EIGHTH_NOTE

    def create_instance_with_no_standart_duration_test(self):
        printTestHeader(
            "Note Test", "create_instance_with_no_standart_duration_test")
        note = Note(Sounds.A, 3, 0.126)
        assert note.get_sound() == Sounds.A
        assert note.get_octave() == 3
        assert note.get_duration() == 0.126


if __name__ == '__main__':
    unittest.main()
