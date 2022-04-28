# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 0:
            return nums

        result = []
        for perm in self.permute(nums[1:]):
            for insertPosition in range(len(perm)+1):
                result.append(perm[:insertPosition] + [nums[0]] + perm[insertPosition:])

        return result

print(sorted(Solution().permute([1,2,3])))
