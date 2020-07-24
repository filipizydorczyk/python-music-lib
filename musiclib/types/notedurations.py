from enum import IntEnum, unique


@unique
class NoteDurations(IntEnum):
    WHOLE_NOTE = 1
    HALF_NOTE = 2
    QUARTER_NOTE = 4
    EIGHTH_NOTE = 8
    SIXTEENTH_NOTE = 16
    THIRTYSECOND_NOTE = 32

    @staticmethod
    def getNoteDurationsFromFloat(x):
        i = int(x ** -1)
        result = None

        try:
            result = NoteDurations(i)
        except ValueError:
            result = None

        return result

    def __float__(self):
        return 1.0 / int(self)

    def __le__(self, other):
        return float(self) <= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __eq__(self, other):
        if other == None:
            float(self) == other
        else:
            return float(self) == float(other)

    def __ne__(self, other):
        if other == None:
            float(self) != other
        else:
            return float(self) != float(other)
