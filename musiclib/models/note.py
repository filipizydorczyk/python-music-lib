from musiclib.types.sounds import Sounds
from musiclib.types.notedurations import NoteDurations
from musiclib.models.pitch import Pitch


class Note:
    """Model representing note"""

    def __init__(self, pitch: Pitch, duration):
        """Creates Note class

        Args:
            pitch (Pitch): pitch of note to be set
            duration (float or NoteDurations): duration how long note will take. If you provide NoteDurations enum it will converted to float.
        """
        self.__pitch = pitch
        self.__duration = float(duration)

    def get_pitch(self) -> Pitch:
        """returns note pitch

        Returns:
            Pitch: pitch of given note
        """
        return self.__pitch

    def get_duration(self):
        """returns dauration given note

        Returns:
            NoteDurations or float: this will return NoteDuartion if float will match and float otherwise
        """
        enm = NoteDurations.getNoteDurationsFromFloat(self.__duration)
        if(enm == None):
            return self.__duration
        else:
            return enm

    def set_duration(self, duration: NoteDurations):
        """change given note duration

        Args:
            duration (NoteDurations): NoteDuration enum to be set
        """
        self.__duration = duration

    def set_duration(self, duration: float):
        """change given note duration

        Args:
            duration (float): duration given with float
        """
        self.__duration = duration

    def set_pitch(self, pitch: Pitch):
        """set pitch of given note

        Args:
            pitch (Pitch): 
        """
        self.__pitch = pitch
