from unittest import TestCase
from PeakIndexInMountainArray import PeakIndexInMountainArray


class TestPeakIndexInMountainArray(TestCase):
    def test_peak_index_in_mountain_array(self):
        self.solution = PeakIndexInMountainArray()
        nums = [0, 1, 0, 3, 4, 1]
        self.assertEqual(self.solution.peakIndexInMountainArray(nums), 4)
        self.assertEqual(self.solution.peakIndexInMountainArray2(nums), 4)
