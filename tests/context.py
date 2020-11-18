from musiclib import Sounds
from musiclib import NoteDurations
from musiclib import Note
from musiclib import Intervals
from musiclib import Chords


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def printTestHeader(header, value):
    print(Bcolors.HEADER + header + Bcolors.ENDC, value)
