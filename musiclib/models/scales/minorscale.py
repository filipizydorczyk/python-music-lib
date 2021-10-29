from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.notesorder import NotesOrder
from musiclib.types.sounds import Sounds


class NaturalMinorScale(Scale):
    """This class contains set of sounds in minor scale for given key.
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(NaturalMinorScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_STEP,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_STEP,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
        ])


class MelodicMinorScale(Scale):
    """The Melodic Minor Scale differs from the Natural Minor Scale by
    the sixth and seventh notes, which are raised one semi-step. This
    scale is kind of peculiar since it is sometimes played differently
    ascending and descending.

    Tips:

    Jazz: The sixth and seventh notes are always raised, exactly as
    the pictures below illustrate. This is the most modern approach
    to this scale.

    Classical music: When you go up the scale, you use the Melodic
    Minor Scale, but when you go down the scale you use the Natural
    Minor Scale. For the Melodic Scale in A, it will look like this:

    :link: https://www.pianoscales.org/minor-melodic.html
    """

    def __init__(self, key: Sounds, notes_order: NotesOrder = NotesOrder.ASCENDING) -> None:

        if(notes_order == NotesOrder.ASCENDING):
            super(MelodicMinorScale, self).__init__(key, [
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
            ])

        if(notes_order == NotesOrder.DESCENDING):
            super(MelodicMinorScale, self).__init__(key, [
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
            ])


class HarmonicMinorScale(Scale):
    """The Harmonic Minor differs from the Natural Minor by 
    the sharpened seventh note, and this minor scale is 
    consequently not played in the same way as the relative 
    major scale. The less common Harmonic Major scale can 
    instead be seen as a relative to the Harmonic minor.

    :link: https://www.pianoscales.org/minor-harmonic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of harmonic minor scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(HarmonicMinorScale, self).__init__(key, [
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.WHOLE_TONE,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,

        ])
