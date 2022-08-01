# https://leetcode.com/problems/non-overlapping-intervals/submissions/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        furthestEnd = intervals[0][1]
        count = 0

        for interval in intervals[1:]:
            if interval[0] < furthestEnd:
                count += 1
                furthestEnd = min(furthestEnd, interval[1])
            else:
                furthestEnd = interval[1]

        return count
