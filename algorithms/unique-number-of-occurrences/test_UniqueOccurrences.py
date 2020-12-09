from unittest import TestCase

from UniqueOccurrences import UniqueOccurrences


class Test(TestCase):
    def test_unique_occurrences(self):
        self.solution = UniqueOccurrences()
        arr = [1, 2, 2, 1, 1, 3]
        self.assertTrue(self.solution.uniqueOccurrences(arr))
