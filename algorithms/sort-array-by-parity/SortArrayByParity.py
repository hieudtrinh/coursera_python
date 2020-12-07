import sys
from typing import List


class SortArrayByParity:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: x % 2)
        return A


def main(argv, arc):
    print(argv, arc)
    arr = [7, 6, 2, 3, 4, 5, 1]
    solution = SortArrayByParity()
    solution.sortArrayByParity(arr)
    print(arr)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
