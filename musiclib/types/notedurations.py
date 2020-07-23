from enum import IntEnum, unique


@unique
class NoteDurations(IntEnum):
    WHOLE_NOTE = 1
    HALF_NOTE = 2
    QUARTER_NOTE = 4
    EIGHTH_NOTE = 8
    SIXTEENTH_NOTE = 16
    THIRTYSECOND_NOTE = 32

    def __float__(self):
        return 1.0 / int(self)
