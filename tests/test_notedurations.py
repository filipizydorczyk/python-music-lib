from .context import NoteDurations, printTestHeader

import unittest


class SoundsTest(unittest.TestCase):

    """Basic test cases."""

    def correct_values_test(self):
        printTestHeader("NoteDaurations Test", "correct_values_test")
        assert float(NoteDurations.WHOLE_NOTE) == 1.0
        assert float(NoteDurations.HALF_NOTE) == 0.5
        assert float(NoteDurations.QUARTER_NOTE) == 0.25
        assert float(NoteDurations.EIGHTH_NOTE) == 0.125
        assert float(NoteDurations.SIXTEENTH_NOTE) == 0.0625
        assert float(NoteDurations.THIRTYSECOND_NOTE) == 0.03125

    def correct_le_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_le_comparing_test")
        assert NoteDurations.WHOLE_NOTE <= NoteDurations.WHOLE_NOTE
        assert NoteDurations.HALF_NOTE <= NoteDurations.WHOLE_NOTE
        assert NoteDurations.QUARTER_NOTE <= NoteDurations.WHOLE_NOTE
        assert NoteDurations.QUARTER_NOTE <= NoteDurations.QUARTER_NOTE
        assert NoteDurations.SIXTEENTH_NOTE <= NoteDurations.QUARTER_NOTE
        assert NoteDurations.THIRTYSECOND_NOTE <= NoteDurations.SIXTEENTH_NOTE
        assert (NoteDurations.SIXTEENTH_NOTE <=
                NoteDurations.THIRTYSECOND_NOTE) == False

    def correct_lt_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_lt_comparing_test")
        assert NoteDurations.HALF_NOTE < NoteDurations.WHOLE_NOTE
        assert NoteDurations.QUARTER_NOTE < NoteDurations.WHOLE_NOTE
        assert NoteDurations.SIXTEENTH_NOTE < NoteDurations.QUARTER_NOTE
        assert NoteDurations.THIRTYSECOND_NOTE < NoteDurations.SIXTEENTH_NOTE
        assert (NoteDurations.SIXTEENTH_NOTE <
                NoteDurations.THIRTYSECOND_NOTE) == False

    def correct_ge_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_ge_comparing_test")
        assert NoteDurations.WHOLE_NOTE >= NoteDurations.WHOLE_NOTE
        assert NoteDurations.WHOLE_NOTE >= NoteDurations.HALF_NOTE
        assert NoteDurations.HALF_NOTE >= NoteDurations.QUARTER_NOTE
        assert NoteDurations.QUARTER_NOTE >= NoteDurations.QUARTER_NOTE
        assert NoteDurations.SIXTEENTH_NOTE >= NoteDurations.SIXTEENTH_NOTE
        assert NoteDurations.SIXTEENTH_NOTE >= NoteDurations.THIRTYSECOND_NOTE
        assert (NoteDurations.THIRTYSECOND_NOTE >=
                NoteDurations.SIXTEENTH_NOTE) == False

    def correct_gt_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_gt_comparing_test")
        assert (NoteDurations.WHOLE_NOTE > NoteDurations.WHOLE_NOTE) == False
        assert NoteDurations.WHOLE_NOTE > NoteDurations.HALF_NOTE
        assert NoteDurations.HALF_NOTE > NoteDurations.QUARTER_NOTE
        assert (NoteDurations.QUARTER_NOTE >
                NoteDurations.QUARTER_NOTE) == False
        assert NoteDurations.SIXTEENTH_NOTE > NoteDurations.THIRTYSECOND_NOTE
        assert (NoteDurations.THIRTYSECOND_NOTE >
                NoteDurations.SIXTEENTH_NOTE) == False

    def correct_eq_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_eq_comparing_test")
        assert NoteDurations.WHOLE_NOTE == NoteDurations.WHOLE_NOTE
        assert NoteDurations.HALF_NOTE == NoteDurations.HALF_NOTE
        assert NoteDurations.QUARTER_NOTE == NoteDurations.QUARTER_NOTE
        assert NoteDurations.SIXTEENTH_NOTE == NoteDurations.SIXTEENTH_NOTE
        assert NoteDurations.THIRTYSECOND_NOTE == NoteDurations.THIRTYSECOND_NOTE
        assert (NoteDurations.SIXTEENTH_NOTE ==
                NoteDurations.THIRTYSECOND_NOTE) == False
        # assert (NoteDurations.SIXTEENTH_NOTE ==
        #         None) == False

    def correct_ne_comparing_test(self):
        printTestHeader("NoteDaurations Test", "correct_ne_comparing_test")
        assert NoteDurations.WHOLE_NOTE != NoteDurations.HALF_NOTE
        assert NoteDurations.HALF_NOTE != NoteDurations.WHOLE_NOTE
        assert NoteDurations.QUARTER_NOTE != NoteDurations.HALF_NOTE
        assert NoteDurations.SIXTEENTH_NOTE != NoteDurations.QUARTER_NOTE
        assert NoteDurations.THIRTYSECOND_NOTE != NoteDurations.SIXTEENTH_NOTE
        assert (NoteDurations.SIXTEENTH_NOTE !=
                NoteDurations.SIXTEENTH_NOTE) == False
        # assert NoteDurations.THIRTYSECOND_NOTE != None

    def getting_duartion_from_float_success_test(self):
        printTestHeader("NoteDaurations Test",
                        "getting_duartion_from_float_success_test")
        assert NoteDurations.getNoteDurationsFromFloat(
            0.125) == NoteDurations.EIGHTH_NOTE

    def getting_duartion_from_float_failed_test(self):
        printTestHeader("NoteDaurations Test",
                        "getting_duartion_from_float_failed_test")
        assert NoteDurations.getNoteDurationsFromFloat(0.126) == None


if __name__ == '__main__':
    unittest.main()
