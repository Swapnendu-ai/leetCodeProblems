# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1

        totalCount = sum(s1Count.values())

        def s2Count(s2):
            if len(s2) < len(s1):
                return False
            start = 0
            end = start

            s2CountDict = defaultdict(int)
            while end < len(s2) and s2[end] in s1Count:
                s2CountDict[s2[end]] += 1
                if end-start + 1 == totalCount:
                    if s1Count == s2CountDict:
                        return True
                    s2CountDict[s2[start]] -= 1
                    start += 1
                end += 1

            if end == len(s2):
                return False

            return s2Count(s2[end+1:])

        return s2Count(s2)
