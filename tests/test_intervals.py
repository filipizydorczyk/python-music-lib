from .context import Intervals, printTestHeader

import unittest


class IntervalsTest(unittest.TestCase):
    """Basic test cases."""

    def create_by_semitones_test(self):
        printTestHeader("Intervals Test", "create_instance_test")
        i = Intervals.getIntervalBySemitones(2)
        assert int(i) == 2

    def create_by_semitones_test(self):
        printTestHeader("Intervals Test", "create_instance_test")
        i = Intervals.getIntervalBySemitones(2)
        assert int(i) == 2
