# https://leetcode.com/problems/meeting-rooms-ii/

from typing import List

from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def getFirstElement(l):
            return l[0]

        if not intervals:
            return 0

        points = defaultdict(int)
        for interval in intervals:
            for i in range(2):
                points[interval[i]] += -1 if i else 1

        count = 0
        maxCount = 0

        for _, numIntervalChange in sorted(points.items(),key=getFirstElement):
            count += numIntervalChange
            maxCount = max(count,maxCount)

        return maxCount

print(Solution().minMeetingRooms([[0,30],[5,10],[15,20]]))
print(Solution().minMeetingRooms([[13,15],[1,13]]))
print(Solution().minMeetingRooms([[9,10],[4,9],[4,17]]))
