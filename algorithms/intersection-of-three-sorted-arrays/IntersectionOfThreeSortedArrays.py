import sys
from typing import List


class IntersectionOfThreeSortedArrays:
    def binarySearch(self, arr, x) -> int:
        lo, mi, hi = 0, 0, len(arr) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if arr[mi] < x:
                lo = mi + 1
            elif arr[mi] > x:
                hi = mi - 1
            else:
                return mi
        return -1

    # solution: using binary search
    def arraysIntersection(self, arr1, arr2, arr3):
        return list(filter(lambda i: self.binarySearch(arr2, i) > -1 and self.binarySearch(arr3, i) > -1, arr1))

    # solution: if statement
    def arraysIntersection2(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr4 = []
        for i in arr1:
            if i in arr2:
                if i in arr3:
                    # num = .index(x)
                    arr4.append(i)
        return arr4

    # solution: if statement
    def arraysIntersection3(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr = []
        for i in arr1:
            if i in arr2 and i in arr3:
                arr.append(i)
        return arr

    # solution: using set() and sorted()
    def arraysIntersection4(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return (sorted(set(arr1) & set(arr2) & set(arr3)))


def main(argv, arc):
    solution = IntersectionOfThreeSortedArrays()
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    arr = solution.arraysIntersection(arr1, arr2, arr3)
    print(arr)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
