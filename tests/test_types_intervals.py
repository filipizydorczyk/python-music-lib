import pytest
from .context import Intervals


def test_create_by_semitones():
    i = Intervals.get_interval_by_semitones(2)
    assert int(i) == 2
