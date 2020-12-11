from typing import List


class CanMakeArithmeticProgressionFromSequence:

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        diff = set()
        arr = sorted(arr)
        for i in range(1, len(arr), 1):
            diff.add(arr[i] - arr[i - 1])
        return len(diff) == 1
