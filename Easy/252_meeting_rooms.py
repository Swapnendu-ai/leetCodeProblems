# https://leetcode.com/problems/meeting-rooms/

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def getFirstElement(l):
            return l[0]

        if not intervals:
            return True

        intervals.sort(key = getFirstElement)

        for i,value in enumerate(intervals[1:]):
            if value[0] < intervals[i][-1]:
                return False

        return True
