import collections
from typing import List


class MinCostToMoveChips:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips = collections.Counter(chip % 2 for chip in position)
        return min(chips[0], chips[1]) if len(chips) > 1 else 0