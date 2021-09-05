import pytest
from .context import NoteDurations


def test_correct_values():
    assert float(NoteDurations.WHOLE_NOTE) == 1.0
    assert float(NoteDurations.HALF_NOTE) == 0.5
    assert float(NoteDurations.QUARTER_NOTE) == 0.25
    assert float(NoteDurations.EIGHTH_NOTE) == 0.125
    assert float(NoteDurations.SIXTEENTH_NOTE) == 0.0625
    assert float(NoteDurations.THIRTYSECOND_NOTE) == 0.03125


def test_correct_le_comparing():
    assert NoteDurations.WHOLE_NOTE <= NoteDurations.WHOLE_NOTE
    assert NoteDurations.HALF_NOTE <= NoteDurations.WHOLE_NOTE
    assert NoteDurations.QUARTER_NOTE <= NoteDurations.WHOLE_NOTE
    assert NoteDurations.QUARTER_NOTE <= NoteDurations.QUARTER_NOTE
    assert NoteDurations.SIXTEENTH_NOTE <= NoteDurations.QUARTER_NOTE
    assert NoteDurations.THIRTYSECOND_NOTE <= NoteDurations.SIXTEENTH_NOTE
    assert (NoteDurations.SIXTEENTH_NOTE <=
            NoteDurations.THIRTYSECOND_NOTE) == False


def test_correct_lt_comparing():
    assert NoteDurations.HALF_NOTE < NoteDurations.WHOLE_NOTE
    assert NoteDurations.QUARTER_NOTE < NoteDurations.WHOLE_NOTE
    assert NoteDurations.SIXTEENTH_NOTE < NoteDurations.QUARTER_NOTE
    assert NoteDurations.THIRTYSECOND_NOTE < NoteDurations.SIXTEENTH_NOTE
    assert (NoteDurations.SIXTEENTH_NOTE <
            NoteDurations.THIRTYSECOND_NOTE) == False


def test_correct_ge_comparing():
    assert NoteDurations.WHOLE_NOTE >= NoteDurations.WHOLE_NOTE
    assert NoteDurations.WHOLE_NOTE >= NoteDurations.HALF_NOTE
    assert NoteDurations.HALF_NOTE >= NoteDurations.QUARTER_NOTE
    assert NoteDurations.QUARTER_NOTE >= NoteDurations.QUARTER_NOTE
    assert NoteDurations.SIXTEENTH_NOTE >= NoteDurations.SIXTEENTH_NOTE
    assert NoteDurations.SIXTEENTH_NOTE >= NoteDurations.THIRTYSECOND_NOTE
    assert (NoteDurations.THIRTYSECOND_NOTE >=
            NoteDurations.SIXTEENTH_NOTE) == False


def test_correct_gt_comparing():
    assert (NoteDurations.WHOLE_NOTE > NoteDurations.WHOLE_NOTE) == False
    assert NoteDurations.WHOLE_NOTE > NoteDurations.HALF_NOTE
    assert NoteDurations.HALF_NOTE > NoteDurations.QUARTER_NOTE
    assert (NoteDurations.QUARTER_NOTE >
            NoteDurations.QUARTER_NOTE) == False
    assert NoteDurations.SIXTEENTH_NOTE > NoteDurations.THIRTYSECOND_NOTE
    assert (NoteDurations.THIRTYSECOND_NOTE >
            NoteDurations.SIXTEENTH_NOTE) == False


def test_correct_eq_comparing():
    assert NoteDurations.WHOLE_NOTE == NoteDurations.WHOLE_NOTE
    assert NoteDurations.HALF_NOTE == NoteDurations.HALF_NOTE
    assert NoteDurations.QUARTER_NOTE == NoteDurations.QUARTER_NOTE
    assert NoteDurations.SIXTEENTH_NOTE == NoteDurations.SIXTEENTH_NOTE
    assert NoteDurations.THIRTYSECOND_NOTE == NoteDurations.THIRTYSECOND_NOTE
    assert (NoteDurations.SIXTEENTH_NOTE ==
            NoteDurations.THIRTYSECOND_NOTE) == False
    assert (NoteDurations.SIXTEENTH_NOTE ==
            None) == False


def test_correct_ne_comparing():
    assert NoteDurations.WHOLE_NOTE != NoteDurations.HALF_NOTE
    assert NoteDurations.HALF_NOTE != NoteDurations.WHOLE_NOTE
    assert NoteDurations.QUARTER_NOTE != NoteDurations.HALF_NOTE
    assert NoteDurations.SIXTEENTH_NOTE != NoteDurations.QUARTER_NOTE
    assert NoteDurations.THIRTYSECOND_NOTE != NoteDurations.SIXTEENTH_NOTE
    assert (NoteDurations.SIXTEENTH_NOTE !=
            NoteDurations.SIXTEENTH_NOTE) == False
    assert NoteDurations.THIRTYSECOND_NOTE != None


def test_getting_duartion_from_float_success():
    assert NoteDurations.get_note_durations_from_float(
        0.125) == NoteDurations.EIGHTH_NOTE


def test_getting_duartion_from_float_failed():
    assert NoteDurations.get_note_durations_from_float(0.126) == None
