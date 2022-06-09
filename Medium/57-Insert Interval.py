# https://leetcode.com/problems/insert-interval/submissions/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        usedNewInterval = False
        result = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                if not usedNewInterval:
                    usedNewInterval = True
                    result.append(newInterval)
                result.append(interval)
            elif newInterval[0] < interval[0]:
                newInterval = [newInterval[0], max(
                    newInterval[1], interval[1])]
            elif newInterval[0] <= interval[1]:
                newInterval = [interval[0], max(newInterval[1], interval[1])]
            else:
                result.append(interval)

        if not usedNewInterval:
            result.append(newInterval)

        return result
