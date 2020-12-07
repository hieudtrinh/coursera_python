from unittest import TestCase
from SelfDividingNumbers import SelfDividingNumbers


class TestSelfDividingNumbers(TestCase):
    def test_self_dividing_numbers(self):
        self.solution = SelfDividingNumbers()
        ans = self.solution.selfDividingNumbers(1, 22)
        print(ans)
