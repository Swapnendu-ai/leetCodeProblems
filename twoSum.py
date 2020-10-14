#problem url: https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndexPair = {}
        for index,num in enumerate(nums):
            leftover = target - num
            try:
                return [index,valueIndexPair[leftover]]
            except KeyError:
                valueIndexPair[num] = index
