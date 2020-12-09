import collections
from typing import List


class UniqueOccurrences:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = collections.Counter(arr)
        return len(m) == len(set(m.values()))
