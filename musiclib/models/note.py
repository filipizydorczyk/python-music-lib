
from musiclib.types.notedurations import NoteDurations
from musiclib.models.pitch import Pitch


class Note:
    """Model representing note"""

    def __init__(self, pitch: Pitch, duration):
        """Creates Note class

        :param pitch: pitch of note to be set
        :type pitch: Pitch
        :param duration: duration how long note will take. If you provide NoteDurations enum it will converted to float.
        :type duration: float or NoteDurations
        """
        self.__pitch = pitch
        self.__duration = float(duration)

    def get_pitch(self) -> Pitch:
        """returns note pitch

        :return: pitch of given note
        :rtype: Pitch
        """
        return self.__pitch

    def get_duration(self):
        """returns dauration given note

        :return: this will return NoteDuartion if float will match and float otherwise
        :rtype: NoteDurations or float
        """
        enm = NoteDurations.get_note_durations_from_float(self.__duration)
        if(enm == None):
            return self.__duration
        else:
            return enm

    def set_duration(self, duration: NoteDurations):
        """change given note duration

        :param duration: NoteDuration enum to be set
        :type duration: NoteDurations
        """
        self.__duration = duration

    def set_duration(self, duration: float):
        """change given note duration

        :param duration: duration given with float
        :type duration: float
        """
        self.__duration = duration

    def set_pitch(self, pitch: Pitch):
        """set pitch of given note

        :param pitch: pitch of note
        :type pitch: Pitch
        """
        self.__pitch = pitch
