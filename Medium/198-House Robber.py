# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        robbedSuffix = [-1] * len(nums)

        def robHelper(position):
            if robbedSuffix[position] != -1:
                return robbedSuffix[position]
            if position == len(nums)-1:
                robbedSuffix[position] = nums[position]
                return robbedSuffix[position]
            if position == len(nums)-2:
                robbedSuffix[position] = max(
                    nums[position], robHelper(position+1))
                return robbedSuffix[position]

            robbedSuffix[position] = max(
                robHelper(position+1),
                nums[position] + robHelper(position+2)
            )
            return robbedSuffix[position]

        return robHelper(0)
