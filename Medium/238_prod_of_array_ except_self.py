# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        prodLeft = prodRight = 1

        for i in range(len(nums)):
            result[i] *= prodLeft
            prodLeft *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            result[i] *= prodRight
            prodRight *= nums[i]

        return result
