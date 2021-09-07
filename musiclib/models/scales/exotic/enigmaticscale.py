from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.notesorder import NotesOrder
from musiclib.types.sounds import Sounds


class EnigmaticMajorScale(Scale):
    """The Enigmatic Scale was invented by the Italian composer Giuseppe Verdi. 
    It is a somewhat obscure augmented scale with an unstable tonic.

    Notice that the Enigmatic Scale is played differently, with one variation, 
    ascending and descending. Verdi is not the only composer connection with a 
    certain scale, for example Béla Bartók is associated with the Lydian Dominant, 
    not as an inventor, but a popularizer.

    :link: https://www.pianoscales.org/enigmatic.html
    :link: https://www.youtube.com/watch?v=UspWDE3gN0A
    :link: https://www.youtube.com/watch?v=cDl3g-JkX08
    :link: https://chord.rocks/guitar/scales/c-enigmatic-ascending
    :link: https://chord.rocks/guitar/scales/c-enigmatic-descending
    """

    def __init__(self, key: Sounds, notes_order=NotesOrder.ASCENDING) -> None:
        """creates instance of enigmatic major scale for given key

        :param key: key of scale
        :type key: Sounds
        :param notes_order: since this scale can be built in diffrent ways
            u need to determin which one u want. By default is is ascending
        :type notes_order: NotesOrder
        """
        if(notes_order == NotesOrder.ASCENDING):
            super(EnigmaticMajorScale, self).__init__(key, [
                Intervals.HALF_TONE,
                Intervals.MINOR_THIRD,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.HALF_TONE,
            ])

        if(notes_order == NotesOrder.DESCENDING):
            super(EnigmaticMajorScale, self).__init__(key, [
                Intervals.HALF_TONE,
                Intervals.MINOR_THIRD,
                Intervals.HALF_TONE,
                Intervals.MINOR_THIRD,
                Intervals.WHOLE_TONE,
                Intervals.HALF_TONE,
                Intervals.HALF_TONE,
            ])


class EnigmaticMinorScale(Scale):
    """Here are pictures and notes of the Minor Enigmatic scales 
    (notice that the minor version is not associated with Giuseppe 
    Verdi).


    :link: https://www.pianoscales.org/enigmatic.html
    """

    def __init__(self, key: Sounds) -> None:
        """creates instance of enigmatic minor scale scale for given key

        :param key: key of scale
        :type key: Sounds
        """

        super(EnigmaticMinorScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.MINOR_THIRD,
            Intervals.HALF_TONE,
            Intervals.HALF_TONE,
        ])
