from unittest import TestCase

from HeightChecker import HeightChecker


class TestHeightChecker(TestCase):
    def test_height_checker(self):
        self.solution = HeightChecker()
        heights = [1, 1, 4, 2, 1, 3]
        self.assertEqual(self.solution.heightChecker(heights), 3)
        self.assertEqual(self.solution.heightChecker2(heights), 3)
