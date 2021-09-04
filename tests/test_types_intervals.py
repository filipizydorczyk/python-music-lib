import pytest
from .context import Intervals, printTestHeader


def test_create_by_semitones():
    printTestHeader("Intervals Test", "test_create_by_semitones")
    i = Intervals.getIntervalBySemitones(2)
    assert int(i) == 2
