class Note:
    """Single Note class """

    def __init__(self, sound, octave, duration):
        """
        Create new note by providing sound, octave, and duration.
        Sound is Sound enum
        Octave is int >= 0
        Duration is Enum or just float. 1.0 Is equalivent of whole note
        """
        self.__octave = octave
        self.__sound = sound
