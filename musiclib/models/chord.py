from musiclib.types.notedurations import NoteDurations
from musiclib.models.pitch import Pitch


class Chord:
    """model representing chord
    """

    def __init__(self, pitches: list, duration):
        """creates new instance of Chord

        Args:
            pitches (list): list of chords Pitch'es
            duration (NoteDurations or float): it can be either float or notedurations enum. Object will store this information as float 
        """
        self.__pitches = pitches
        self.__duration = duration

    def get_pitches(self) -> list:
        """get Pitch'es list of chord

        Returns:
            list: list of Pitch elements
        """
        return self.__pitches

    def get_duration(self) -> float:
        """get chord durations

        Returns:
            float: returns note duration in float, if duration was provided as NoteDurations enum it can be converted back
        """
        return self.__duration
