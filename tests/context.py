from typing import Set
from musiclib import *


def scale_comparator(scale: Scale, desired_result: Set[Sounds]) -> bool:
    """function to test scales

    :param scale: scale to test
    :type scale: Scale
    :param desired_result: set of sounds u expect to be in created scale
    :type desired_result: Set[Sounds]
    :return: is scale same as provided sounds
    :rtype: bool
    """

    actual_result = scale.get_scale_sounds()
    print("Diff: ", desired_result.symmetric_difference(actual_result))
    return len(desired_result.symmetric_difference(actual_result)) == 0
