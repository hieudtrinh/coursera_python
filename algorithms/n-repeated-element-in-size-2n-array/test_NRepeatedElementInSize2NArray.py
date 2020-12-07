from unittest import TestCase
from NRepeatedElementInSize2NArray import NRepeatedElementInSize2NArray


class TestNRepeatedElementInSize2NArray(TestCase):
    def test_repeated_ntimes2(self):
        self.solution = NRepeatedElementInSize2NArray()
        self.assertEqual(self.solution.repeatedNTimes([1,2,3,3]), 3)
        self.assertEqual(self.solution.repeatedNTimes([2,1,2,5,3,2]), 2)
        self.assertEqual(self.solution.repeatedNTimes([5,1,5,2,5,3,5,4]), 5)
