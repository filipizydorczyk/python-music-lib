from enum import IntEnum, Enum, auto


class Dynamics(IntEnum):
    """Dynamics markings
    In music, the dynamics of a piece is the variation in loudness between notes or phrases. Dynamics are indicated by specific musical notation, often in some detail.
    Generally volume of each dynamic is contractual and if this enums will be used in anything u will have to define volumes for each dynamic.
    Meaning of dynamics wold be somthing like that

    fortississimo   fff very very loud

    fortissimo      ff  very loud 

    forte           f   loud

    mezzo-forte     mf  average

    mezzo-piano     mp  average

    piano           p   quiet

    pianissimo      pp  very quiet

    pianississimo   ppp very very quiet


    You can read more on wikipedia.

    :link: https://en.wikipedia.org/wiki/Dynamics_(music)
    """

    PIANISSISSIMO = 0,
    PIANISSIMO = 1,
    PIANO = 2,
    MEZZO_PIANO = 3,
    MEZZO_FORTE = 4,
    FORTE = 5,
    FORTISSIMO = 6,
    FORTISSISSIMO = 7


class Changes(Enum):
    """Changes

    Three Italian words are used to show gradual changes in volume: 
     - crescendo translates as "increasing" (literally "growing")
     - decrescendo translates as "decreasing".
     - diminuendo translates as "diminishing".

    You can read more on wikipedia.

    :link: https://en.wikipedia.org/wiki/Dynamics_(music)
    """
    CRESCENDO = auto(),
    DECRESCENDO = auto(),
    DIMINUENDO = auto()
