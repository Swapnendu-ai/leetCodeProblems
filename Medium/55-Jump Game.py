# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canJumpTable = [None] * (len(nums)-1) + [True]

        def canJumpHelper(index):
            if canJumpTable[index] is not None:
                return canJumpTable[index]
            if nums[index] <= 0:
                canJumpTable[index] = False
                return False
            jumpSteps = nums[index]
            for nextIndex in range(min(len(nums)-1, index+jumpSteps), index, -1):
                canReachEnd = canJumpHelper(nextIndex)
                if canReachEnd:
                    canJumpTable[index] = True
                    return True
            canJumpTable[index] = False
            return False
        return canJumpHelper(0)
