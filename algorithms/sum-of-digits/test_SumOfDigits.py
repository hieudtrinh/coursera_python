from unittest import TestCase

from SumOfDigits import SumOfDigits


class TestSumOfDigits(TestCase):
    def test_sum_of_digits(self):
        self.solution = SumOfDigits()
        arr = [17, 26, 32, 53, 64, 25, 123]
        print(arr)
        print(self.solution.sumOfDigits(arr))
