# https://leetcode.com/problems/jump-game-ii/submissions/

class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        maxReachable = -1
        indexWithMaxReachable = 0
        numberOfJumps = 0
        while start != len(nums)-1:
            # print(start)
            numberOfJumps += 1
            if start + nums[start] >= len(nums) - 1:
                return numberOfJumps
            if nums[start] == 0:
                return 0
            for nextIndex in range(start+1, 1+min(len(nums)-1, start+nums[start])):
                if nextIndex + nums[nextIndex] >= maxReachable:
                    maxReachable = nextIndex + nums[nextIndex]
                    indexWithMaxReachable = nextIndex
            start = indexWithMaxReachable

        return 0
