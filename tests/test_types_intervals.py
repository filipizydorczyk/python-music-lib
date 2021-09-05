import pytest
from .context import Intervals


def test_create_by_semitones():
    i = Intervals.getIntervalBySemitones(2)
    assert int(i) == 2
