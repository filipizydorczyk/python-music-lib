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
