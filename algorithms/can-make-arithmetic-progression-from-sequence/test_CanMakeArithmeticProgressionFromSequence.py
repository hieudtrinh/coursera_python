from unittest import TestCase

from CanMakeArithmeticProgressionFromSequence import CanMakeArithmeticProgressionFromSequence


class TestCanMakeArithmeticProgressionFromSequence(TestCase):
    def test_can_make_arithmetic_progression(self):
        self.solution = CanMakeArithmeticProgressionFromSequence()
        arr = [5, 1, 3]
        self.assertTrue(self.solution.canMakeArithmeticProgression(arr))
        arr = [1, 4, 2]
        self.assertFalse(self.solution.canMakeArithmeticProgression(arr))

