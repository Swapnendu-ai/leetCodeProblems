# https://leetcode.com/problems/subsets/submissions/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        subsetsWithoutLast = self.subsets(nums[:-1])
        subsets = []
        for subset in subsetsWithoutLast:
            subsets.append(subset.copy())
            subset.append(nums[-1])
            subsets.append(subset)

        return subsets
