from musiclib.types.intervals import Intervals
from musiclib.types.sounds import Sounds


class CircleOfFifths:
    """In music theory, the circle of fifths is a way of organizing 
    the 12 chromatic pitches as a sequence of perfect fifths. 
    If C is chosen as a starting point, the sequence is: C, G, D, A

    This collection represents Circle of fifths. You can access
    elements just like you were using list `Circle()[1]`. You can 
    provide each number you want to so if you for example provide
    something like this Circle()[-1] it will go back in a circle.

    :link: https://en.wikipedia.org/wiki/Circle_of_fifths
    """

    def __init__(self, sound: Sounds = Sounds.C) -> None:
        """Creates new circle of fiths instance. By defult C is first
        sound by you can specify first element by passing Sounds enum
        to constructor.

        :param sound: sound that circle should put as first, defaults 
        to Sounds.C
        :type sound: Sounds, optional
        """
        self.__sounds_order = []

        for i in range(12):
            self.__sounds_order.append(sound.add(i*Intervals.PERFECT_FIFTH))

    def __getitem__(self, index):
        return self.__sounds_order[index % 12]
