from functools import reduce
from typing import List


class ArrayPartition:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return reduce(lambda acc, x: acc + min(nums[x], nums[x + 1]), range(0, len(nums), 2), 0)

    def arrayPairSum2(self, nums: List[int]) -> int:
        # print(sorted(nums)[::2])
        return sum(sorted(nums)[::2])
