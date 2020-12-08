from typing import List


class SquaresOfASortedArray:
    # Runtime: 500 ms, faster than 5.06%
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r,ans=0,len(nums)-1,[]
        while l<=r:
            if abs(nums[r]) > abs(nums[l]):
                ans.insert(0, nums[r] * nums[r])
                r-=1
            else:
                ans.insert(0, nums[l] * nums[l])
                l+=1
        return ans

    # Runtime: 300 ms
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        return sorted([n * n for n in nums])