## Intervals

`musiclib/types/intervals.py`

Enumerate containing music intervals, and related methods

Semitone is smallest distance between sounds.

```
C -> C is 0 semitones
C -> Cis is 1 semitones
C -> D is 2 semitones
C -> Dis is 3 semitones
...
```

### Values

| SEMITONES | PERFECT INTERVALS        | AUGMENTED OR DIMINISHED INTERVALS                     | ALTERNATIVE NAMES                                          |
| --------- | ------------------------ | ----------------------------------------------------- | ---------------------------------------------------------- |
| 0         | Intervals.PERFECT_UNISON | Intervals.DIMINISHED_SECOND                           |                                                            |
| 1         | Intervals.MINOR_SECOND   | Intervals.AUGMENTED_UNISON                            | Intervals.SEMITONE,Intervals.HALF_STEP,Intervals.HALF_TONE |
| 2         | Intervals.MAJOR_SECOND   | Intervals.DIMINISHED_THRD                             | Intervals.TONE,Intervals.WHOLE_TONE,Intervals.WHOLE_STEP   |
| 3         | Intervals.MINOR_THIRD    | Intervals.AUGMENTED_SECOND                            |                                                            |
| 4         | Intervals.MAJOR_THIRD    | Intervals.DIMINISHED_FOURTH                           |                                                            |
| 5         | Intervals.PERFECT_FOURTH | Intervals.AUGMENTED_THIRD                             |                                                            |
| 6         |                          | Intervals.DIMINISHED_FIFTH,Intervals.AUGMENTED_FOURTH | Intervals.TRITONE                                          |
| 7         | Intervals.PERFECT_FIFTH  | Intervals.DIMINISHED_SIXTH                            |                                                            |
| 8         | Intervals.MINOR_SIXTH    | Intervals.AUGMENTED_FIFTH                             |                                                            |
| 9         | Intervals.MAJOR_SIXTH    | Intervals.DIMINISHED_SEVENTH                          |                                                            |
| 10        | Intervals.MINOR_SEVENTH  | Intervals.AUGMENTED_SIXTH                             |                                                            |
| 11        | Intervals.MAJOR_SEVENTH  | Intervals.DIMINISHED_OCTAVE                           |                                                            |
| 12        | Intervals.PERFECT_OCTAVE | Intervals.AUGMENTED_SEVENTH                           |                                                            |

### Methods

#### getIntervalsSemitone

```py
@staticmethod
def getIntervalBySemitones(semitones: int):
```

Static method that returns Interval adequate to given semitone numners
Semitone is int i <0;12>

```py
from musiclib import NoteDurations

assert NoteDurations.getNoteDurationsFromFloat(0.125) == NoteDurations.EIGHTH_NOTE
assert NoteDurations.getNoteDurationsFromFloat(0.126) == None
```
