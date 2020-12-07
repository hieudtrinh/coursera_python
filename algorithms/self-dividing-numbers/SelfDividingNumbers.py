import sys
from typing import List


class SelfDividingNumbers:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            for x in map(int, str(i)):
                if x == 0 or i % x != 0:
                    break
            else:
                res.append(i)
        return res


def main(argv, arc):
    print(argv, arc)
    solution = SelfDividingNumbers()
    arr = solution.selfDividingNumbers(1, 22)
    print(arr)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
