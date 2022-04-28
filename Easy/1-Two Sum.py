#problem url: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        balanceToIndex = {}
        for i, num in enumerate(nums):
            if num in balanceToIndex:
                return [i, balanceToIndex[num]]
            balanceToIndex[target-num] = i
