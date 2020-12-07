from unittest import TestCase

from SortArrayByParity import SortArrayByParity


class TestSortArrayByParity(TestCase):
    def test_sort_array_by_parity(self):
        self.solution = SortArrayByParity()
        A = [7, 6, 2, 3, 4, 5, 1]
        self.solution.sortArrayByParity(A)
        print(A)
