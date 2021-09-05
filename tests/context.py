from typing import Set
from musiclib import Sounds
from musiclib import NoteDurations
from musiclib import Note
from musiclib import Intervals
from musiclib import Chords
from musiclib import Pitch
from musiclib import PitchesList
from musiclib import create_major_chord
from musiclib import create_minor_chord
from musiclib import create
from musiclib import MajorScale
from musiclib import MinorScale
from musiclib import WholeToneScale
from musiclib import AlgerianScales
from musiclib import ArabicScale
from musiclib import AugmentedScale
from musiclib import BalineseScale
from musiclib import ByzantineScale
from musiclib import ChineseScale
from musiclib import Scale


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def scale_comparator(scale: Scale, desired_result: Set[Sounds]):
    actual_result = scale.get_scale_sounds()
    return len(desired_result.symmetric_difference(actual_result)) == 0
