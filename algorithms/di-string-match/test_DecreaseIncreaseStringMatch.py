from unittest import TestCase
from DecreaseIncreaseStringMatch import DecreaseIncreaseStringMatch


class TestDecreaseIncreaseStringMatch(TestCase):
    def test_di_string_match(self):
        self.solution = DecreaseIncreaseStringMatch()
        S = "IDID"
        arr = self.solution.diStringMatch(S)
        expect_ans = [0, 4, 1, 3, 2]
        self.assertEqual(arr, expect_ans)

