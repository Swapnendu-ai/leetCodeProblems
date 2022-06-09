# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)
        maxStreakLen = 0
        visited = set()
        for num in numsSet:
            streakLen = 0
            if num not in visited:
                visited.add(num)
                streakLen += 1
                prevNum = num - 1
                while prevNum in numsSet:
                    visited.add(prevNum)
                    streakLen += 1
                    prevNum -= 1
                nextNum = num + 1
                while nextNum in numsSet:
                    visited.add(nextNum)
                    streakLen += 1
                    nextNum += 1
                #print(visited)
                maxStreakLen = max(maxStreakLen, streakLen)

        return maxStreakLen
