from .context import Sounds

import unittest


class SoundsTest(unittest.TestCase):

    """Basic test cases."""

    def correct_values_test(self):
        assert int(Sounds.C) == 1
        assert int(Sounds.CIS) == 2
        assert int(Sounds.D) == 3
        assert int(Sounds.DIS) == 4
        assert int(Sounds.E) == 5
        assert int(Sounds.F) == 6
        assert int(Sounds.FIS) == 7
        assert int(Sounds.G) == 8
        assert int(Sounds.GIS) == 9
        assert int(Sounds.A) == 10
        assert int(Sounds.AIS) == 11
        assert int(Sounds.B) == 12


if __name__ == '__main__':
    unittest.main()
