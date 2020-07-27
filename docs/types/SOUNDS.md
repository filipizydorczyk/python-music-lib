## Sounds

`musiclib/types/sounds.py`

This types contains typical sounds for 12 equal temperament system. So in this case CIS is same ad D flat. Maybe in future there will be more tuning system available. Rest is no sound at all.

### Values

```py
@unique
class Sounds(IntEnum):
    """Music sounds"""
    REST = 0
    C = 1
    CIS = 2
    D = 3
    DIS = 4
    E = 5
    F = 6
    FIS = 7
    G = 8
    GIS = 9
    A = 10
    AIS = 11
    B = 12

```
