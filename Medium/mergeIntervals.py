# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def getFirstElement(l:List[int]) -> int:
            return l[0]

        if not intervals:
            return intervals

        result = []
        intervals.sort(key=getFirstElement)
        low = intervals[0][0]
        hi = intervals[0][-1]

        for interval in intervals:
            newLo, newHi = interval[0],interval[-1]
            if newLo <= hi:
                hi = max(hi,newHi)
            else:
                result.append([low,hi])
                low = newLo
                hi = newHi
        result.append([low,hi])
        return result

print(Solution().merge([[1,4],[4,5]]))

