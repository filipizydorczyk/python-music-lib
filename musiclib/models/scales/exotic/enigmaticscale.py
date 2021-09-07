from musiclib.models.scales.scale import Scale
from musiclib.types.intervals import Intervals
from musiclib.types.notesorder import NotesOrder
from musiclib.types.sounds import Sounds


class EnigmaticScale(Scale):
    """The Enigmatic Scale was invented by the Italian composer Giuseppe Verdi. 
    It is a somewhat obscure augmented scale with an unstable tonic.

    Notice that the Enigmatic Scale is played differently, with one variation, 
    ascending and descending. The diagrams show the ascending versions of the scale, 
    with the notes for the descending scale written out below. Verdi is not the only 
    composer connection with a certain scale, for example Béla Bartók is associated 
    with the Lydian Dominant, not as an inventor, but a popularizer.

    :link: https://www.pianoscales.org/enigmatic.html
    """

    def __init__(self, key: Sounds, notes_order=NotesOrder.ASCENDING) -> None:
        """creates instance of eight tone spanish scale for given key

        :param key: key of scale
        :type key: Sounds
        :param notes_order: since this scale can be built in diffrent ways
            u need to determin which one u want. By default is is ascending
        :type notes_order: NotesOrder
        """

        super(EnigmaticScale, self).__init__(key, [
            Intervals.HALF_TONE,
            Intervals.WHOLE_TONE
        ])
