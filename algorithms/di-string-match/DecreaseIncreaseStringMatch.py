from typing import List


class DecreaseIncreaseStringMatch:
    def diStringMatch(self, S: str) -> List[int]:
        A = []
        i = 0
        d = len(S)
        for c in S:
            if c == 'I':
                A.append(i)
                i += 1
            else:
                A.append(d)
                d -= 1
        A.append(i)
        return A