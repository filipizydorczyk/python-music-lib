from .context import NoteDurations, printTestHeader

import unittest


class SoundsTest(unittest.TestCase):

    """Basic test cases."""

    def correct_values_test(self):
        assert float(NoteDurations.WHOLE_NOTE) == 1.0
        assert float(NoteDurations.HALF_NOTE) == 0.5
        assert float(NoteDurations.QUARTER_NOTE) == 0.25
        assert float(NoteDurations.EIGHTH_NOTE) == 0.125
        assert float(NoteDurations.SIXTEENTH_NOTE) == 0.0625
        assert float(NoteDurations.THIRTYSECOND_NOTE) == 0.03125

    def correct_lt_comparing_test(self):
        printTestHeader("correct_lt_comparing_test", NoteDurations.WHOLE_NOTE)
        assert NoteDurations.WHOLE_NOTE < NoteDurations.HALF_NOTE
        assert NoteDurations.WHOLE_NOTE < NoteDurations.QUARTER_NOTE
        assert NoteDurations.WHOLE_NOTE < NoteDurations.SIXTEENTH_NOTE
        assert NoteDurations.WHOLE_NOTE < NoteDurations.THIRTYSECOND_NOTE

        printTestHeader("correct_lt_comparing_test", NoteDurations.HALF_NOTE)
        assert NoteDurations.HALF_NOTE < NoteDurations.QUARTER_NOTE
        assert NoteDurations.HALF_NOTE < NoteDurations.SIXTEENTH_NOTE
        assert NoteDurations.HALF_NOTE < NoteDurations.THIRTYSECOND_NOTE

        printTestHeader("correct_lt_comparing_test",
                        NoteDurations.QUARTER_NOTE)
        assert NoteDurations.QUARTER_NOTE < NoteDurations.SIXTEENTH_NOTE
        assert NoteDurations.QUARTER_NOTE < NoteDurations.THIRTYSECOND_NOTE

        printTestHeader("correct_lt_comparing_test",
                        NoteDurations.SIXTEENTH_NOTE)
        assert NoteDurations.SIXTEENTH_NOTE < NoteDurations.THIRTYSECOND_NOTE


if __name__ == '__main__':
    unittest.main()
