from __future__ import annotations
from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class Pitch:
    """Class containing informations about sound and its octave for example A2 or D#3
    """

    def __init__(self, sound: Sounds, octave: int):
        """constructor

        Args:
            sound (Sounds): sound of pitch (A,B,C,C# et.)
            octave (int): octve given as a number
        """
        self.__sound = sound
        self.__octave = octave

    def get_sound(self) -> Sounds:
        """ returns Sound type of given pitch

        Returns:
            Sounds: Sound type of given pitch
        """
        return self.__sound

    def get_octave(self) -> int:
        """returns octave of given pitch

        Returns:
            int: octave of given pitch
        """
        return self.__octave

    def add(self, interval: Intervals) -> Pitch:
        """adds to note given interval

        :param interval: Intervals enum to add to note. Can be also int as semitones 
        :type interval: Intervals
        :return: new instance of Pitch after added interveal
        :rtype: Pitch
        """
        octaves = int(interval) // 12
        semitones = int(interval) % 12

        new_sound = self.__sound.add(semitones)
        new_octave = self.__octave + octaves
        if(new_sound < self.__sound):
            new_octave += 1
        return Pitch(new_sound, new_octave)
