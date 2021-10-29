import pytest

from .context import CircleOfFifths, Sounds


def test_should_create_basic_collection():
    circle = CircleOfFifths()

    assert circle[0] == Sounds.C
    assert circle[1] == Sounds.G
    assert circle[2] == Sounds.D


def test_should_resolve_indexes_correctly():
    circle = CircleOfFifths()

    assert circle[-1] == Sounds.F
    assert circle[12] == Sounds.C
    assert circle[13] == Sounds.G


def test_should_create_collection_with_changed_notes_order():
    circle = CircleOfFifths(Sounds.G)

    assert circle[0] == Sounds.G
    assert circle[1] == Sounds.D
    assert circle[2] == Sounds.A


def test_should_resolve_indexes_correctly_with_changed_order():
    circle = CircleOfFifths(Sounds.G)

    assert circle[-1] == Sounds.C
    assert circle[12] == Sounds.G
    assert circle[13] == Sounds.D
