# https://leetcode.com/problems/next-permutation/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not self.nextPermutationHelper(nums):
            nums.reverse

