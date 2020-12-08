from typing import List


class PeakIndexInMountainArray:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo


    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        def findPeak(arr, left, right):
            if left == right:
                return left
            mid = (left+right)//2
            if arr[mid] < arr[mid+1]:
                return findPeak(arr, mid+1, right)
            else:
                return findPeak(arr, left, mid)


        if len(arr) < 3:
            return -1

        return findPeak(arr, 0, len(arr)-1)


