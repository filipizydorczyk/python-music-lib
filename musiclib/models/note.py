from musiclib.types.sounds import Sounds
from musiclib.types.notedurations import NoteDurations


class Note:
    """Single Note class """

    def __init__(self, sound: Sounds, octave: int, duration):
        """
        Create new note by providing sound, octave, and duration.
        Sound is Sound enum
        Octave is int >= 0
        Duration is Enum or just float. 1.0 Is equalivent of whole note
        """
        self.__octave = octave
        self.__sound = sound
        self.__duration = float(duration)

    def get_octave(self):
        return self.__octave

    def set_octave(self, x):
        self.__octave = x

    def get_sound(self):
        return self.__sound

    def set_sound(self, x):
        self.__sound = x

    def get_duration(self):
        enm = NoteDurations.getNoteDurationsFromFloat(self.__duration)
        if(enm == None):
            return self.__duration
        else:
            return enm

    def set_duration(self, x):
        self.__duration = x
