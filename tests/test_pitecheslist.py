import pytest
from .context import Pitch, Sounds, Intervals, PitchesList


def test_should_add_pitches_after_adding_intervals_to_collection():
    plist = PitchesList()
    plist.append(Pitch(Sounds.A, 4))
    plist.append(Intervals.AUGMENTED_THIRD)
    assert plist[0].get_sound() == Sounds.A
    assert plist[1].get_sound() == Sounds.D


def test_should_add_pithches_to_collection():
    plist = PitchesList()
    plist.append(Pitch(Sounds.A, 4))
    plist.append(Pitch(Sounds.B, 4))
    assert plist[0].get_sound() == Sounds.A
    assert plist[1].get_sound() == Sounds.B


def test_should_not_add_interval_due_to_no_first_element():
    plist = PitchesList()
    plist.append(Intervals.AUGMENTED_SECOND)
    assert len(plist) == 0
