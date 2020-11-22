from __future__ import annotations
from enum import IntEnum


class Intervals(IntEnum):
    PERFECT_UNISON = 0
    DIMINISHED_SECOND = 0

    SEMITONE = 1
    HALF_STEP = 1
    HALF_TONE = 1
    MINOR_SECOND = 1
    AUGMENTED_UNISON = 1

    MAJOR_SECOND = 2
    DIMINISHED_THRD = 2
    TONE = 2
    WHOLE_TONE = 2
    WHOLE_STEP = 2

    MINOR_THIRD = 3
    AUGMENTED_SECOND = 3

    MAJOR_THIRD = 4
    DIMINISHED_FOURTH = 4

    PERFECT_FOURTH = 5
    AUGMENTED_THIRD = 5

    DIMINISHED_FIFTH = 6
    AUGMENTED_FOURTH = 6
    TRITONE = 6

    PERFECT_FIFTH = 7
    DIMINISHED_SIXTH = 7

    MINOR_SIXTH = 8
    AUGMENTED_FIFTH = 8

    MAJOR_SIXTH = 9
    DIMINISHED_SEVENTH = 9

    MINOR_SEVENTH = 10
    AUGMENTED_SIXTH = 10

    MAJOR_SEVENTH = 11
    DIMINISHED_OCTAVE = 11

    PERFECT_OCTAVE = 12
    AUGMENTED_SEVENTH = 12

    @staticmethod
    def getIntervalBySemitones(semitones: int) -> Interval:
        """Static method that returns Interval adequate to given semitone numners. 

        :param semitones: Semitone is int i <0;12>
        :type semitones: int
        :return: emnum Interval
        :rtype: Interval
        """
        return Intervals(semitones)
