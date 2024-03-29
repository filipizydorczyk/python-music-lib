from __future__ import annotations
from musiclib.types.intervals import Intervals
from typing import Union
from enum import IntEnum, unique


@unique
class Sounds(IntEnum):
    """ Music sounds. These are sounds without octaves to add octaves you need to use this enum im Pitch model.
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

    def add(self, semitones: Union[int, Intervals]) -> Sounds:
        """ Move your sound by given steps. If you want to move from C to D# you
        need to add 3. If you will add 12 sound won't change. Higher cycle repeats.
        So if you add 13 you move from C to C#. You will never recive REST enum from
        actual notes like C,D,E etc. If you attepmt to add steps to REST it will stay rest anyway.

        :param semitones: how many steps u want to move your sound.
            It can be provided by amound of semitones or interval name.
        :type semitones: Union[int, Intervals]
        :return: new instance of sound after added given steps
        :rtype: Sounds
        """
        if(self.value == Sounds.REST):
            return Sounds.REST
        new_value = (self.value + semitones) % 12
        if(new_value == 0):
            new_value = 12
        return Sounds(new_value)

    def subtract(self, semitones: Union[int, Intervals]) -> Sounds:
        """It does the same as add method but in descending order instead of
        ascending. You will never recive REST with this method unless current
        sound is REST. Then it will remain rest regardless of provided argument.
        If you substract 1 from C u will get B etc. 

        :param semitones: how many steps u want to move your sound.
            It can be provided by amound of semitones or interval name.
        :type semitones: Union[int, Intervals]
        :return: new instance of sound after added given steps
        :rtype: Sounds
        """
        if(self.value == Sounds.REST):
            return Sounds.REST
        new_value = (self.value - semitones) % 12
        if(new_value == 0):
            new_value = 12
        return Sounds(new_value)

    def flat(self) -> Sounds:
        """It will return current sound decrased by one semitone. In some tunes
        for example g flat can be diffrent sound than fis but at the moment 
        this library assume that we use equal temperament tuning.

        :return: flatted sound
        :rtype: Sounds
        """
        return self.subtract(1)

    def sharp(self) -> Sounds:
        """It will return current sound increased by one semitone. In some tunes
        for example g flat can be diffrent sound than fis but at the moment 
        this library assume that we use equal temperament tuning.

        :return: new sound
        :rtype: Sounds
        """
        return self.add(1)

    def __str__(self) -> str:
        return super().__str__().split(".")[1]
