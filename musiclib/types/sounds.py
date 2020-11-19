from __future__ import annotations
from enum import IntEnum, unique


@unique
class Sounds(IntEnum):
    """ Music sounds. These are sounds without octaves to add octaves you need to use this enum im Pithc model.
        REST is no sound at all.
    """
    REST = 0
    C = 1
    CIS = 2
    D = 3
    DIS = 4
    E = 5
    F = 6
    FIS = 7
    G = 8
    GIS = 9
    A = 10
    AIS = 11
    B = 12

    def add(self, semitones: int) -> Sounds:
        """ Move your sound by given steps. If you want to move from C to D# you
            need to add 3. If you will add 12 sound won't change. Higher cycle repeats.
            So if you add 13 you move from C to C#. You will never recive REST enum from
            actual notes like C,D,E etc. If you attepmt to add steps to REST it will stay rest anyway.

        Args:
            semitones (int): how many steps u want to move your sound

        Returns:
            Sounds: new instance of sound after added given steps
        """
        if(self.value == Sounds.REST):
            return Sounds.REST
        new_value = (self.value + semitones) % 12
        if(new_value == 0):
            new_value = 12
        return Sounds(new_value)
