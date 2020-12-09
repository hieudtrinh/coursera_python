from functools import reduce
from typing import List


class HeightChecker:
    def heightChecker(self, heights: List[int]):
        return reduce(lambda a, s: a + (s[0] != s[1]), zip(heights, sorted(heights)), 0)


    # The zip() function returns a zip object, which is an iterator of tuples where
    # the first item in each passed iterator is paired together, and then the second
    # item in each passed iterator are paired together etc.
    #
    # If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.


    def heightChecker2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cnt=0
        height=sorted(heights)
        for i,j in zip(height,heights):
            if i!=j:
                cnt+=1
        return cnt
