from typing import List


class NRepeatedElementInSize2NArray:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()
        for n in A:
            if n in seen:
                return n
            seen.add(n)


    def repeatedNTimes2(self, A: List[int]) -> int:
        A = sorted(A)
        half = int(len(A)/2)
        if (A[half] == A[half+1]):
            return A[half]
        else:
            return A[half - 1]