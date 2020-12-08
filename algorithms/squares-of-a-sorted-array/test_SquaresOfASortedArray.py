from unittest import TestCase
from SquaresOfASortedArray import SquaresOfASortedArray


class TestSquaresOfASortedArray(TestCase):
    def test_sorted_squares2(self):
        self.solution = SquaresOfASortedArray()
        nums = [-4,-1,0,3,10]
        exp_ans = [0,1,9,16,100]
        ans = self.solution.sortedSquares(nums)
        self.assertEqual(exp_ans, ans)