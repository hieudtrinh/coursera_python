from unittest import TestCase

from ArrayPartition import ArrayPartition


class TestArrayPartition(TestCase):
    def test_array_pair_sum(self):
        self.solution = ArrayPartition()
        nums = [1, 4, 3, 2]
        n = self.solution.arrayPairSum(nums)
        print(n)
        print(self.solution.arrayPairSum2([1, 4, 3, 2]))
