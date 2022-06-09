# https://leetcode.com/problems/permutations/submissions/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        permutations = []

        for num in nums:
            smallerPermutations = self.permute([n for n in nums if n != num])
            for perm in smallerPermutations:
                perm.append(num)
            permutations.extend(smallerPermutations)

        return permutations
