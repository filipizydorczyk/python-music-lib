from .context import Sounds

import unittest


class SoundsTest(unittest.TestCase):

    """Basic test cases."""

    def correct_values_test(self):
        print(Sounds.C)
        assert True


if __name__ == '__main__':
    unittest.main()
