from typing import List
import sys


class ReplaceElementsWithGreatestElementOnRightSide:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rval = -1
        for i in range(len(arr)-1,-1,-1):
            # arr[i], rval = rval, max(arr[i], rval)
            # same as
            cur = arr[i]
            arr[i] = rval
            rval = max(cur, rval)

        return arr

def main(argv, arc):
    print(argv, arc)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))