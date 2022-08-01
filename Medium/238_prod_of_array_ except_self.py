# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for num in nums[:-1]:
            left.append(left[-1]*num)
        for idx in range(len(nums)-1, 0, -1):
            right.append(right[-1]*nums[idx])
        right.reverse()

        answer = []
        for l, r in zip(left, right):
            answer.append(l*r)

        return answer



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
