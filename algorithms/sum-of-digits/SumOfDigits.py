import sys
from typing import List


class SumOfDigits:
    def sumOfDigits(self, A: List[int]) -> int:
        minValue = min(A)
        total = sum(x for x in map(int, str(minValue)))
        print(total)
        return (1 + sum(x for x in map(int, str(min(A))))) % 2


def main(argv, arc):
    print(argv, arc)
    arr = [17, 26, 32, 53, 64, 25, 123]
    solution = SumOfDigits()
    print(solution.sumOfDigits(arr))


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
