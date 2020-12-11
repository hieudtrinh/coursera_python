from unittest import TestCase

from IntersectionOfThreeSortedArrays import IntersectionOfThreeSortedArrays


class TestIntersectionOfThreeSortedArrays(TestCase):
    def test_arrays_intersection4(self):
        self.solution = IntersectionOfThreeSortedArrays()
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [1, 2, 5, 7, 9]
        arr3 = [1, 3, 4, 5, 8]
        ans = [1, 5]
        self.assertEqual(self.solution.arraysIntersection(arr1, arr2, arr3), ans)
        self.assertEqual(self.solution.arraysIntersection2(arr1, arr2, arr3), ans)
        self.assertEqual(self.solution.arraysIntersection3(arr1, arr2, arr3), ans)
        self.assertEqual(self.solution.arraysIntersection4(arr1, arr2, arr3), ans)
