from musiclib.types.notedurations import NoteDurations
from musiclib.models.pitch import Pitch


class Chord:
    """model representing chord
    """

    def __init__(self, pitches: list, duration):
        """creates new instance of Chord

        :param pitches: list of chords Pitch'es
        :type pitches: list
        :param duration: it can be either float or notedurations enum. Object will store this information as float
        :type duration: NoteDurations or float
        """
        self.__pitches = pitches
        self.__duration = duration

    def get_pitches(self) -> list:
        """get Pitch'es list of chord

        :return: list of Pitch elements
        :rtype: list
        """
        return self.__pitches

    def get_duration(self) -> float:
        """get chord durations

        :return: returns note duration in float, if duration was provided as NoteDurations enum it can be converted back
        :rtype: float
        """
        return self.__duration
