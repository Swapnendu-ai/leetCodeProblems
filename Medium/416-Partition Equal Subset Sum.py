# https://leetcode.com/problems/partition-equal-subset-sum/submissions/

class Solution:
    def subsetTarget(self, nums, end, target, table):
        if target == 0:
            return True
        if end == 0:
            return target == nums[0]
        if target in table[end]:
            return table[end][target]

        table[end][target] = self.subsetTarget(
            nums, end-1, target-nums[end], table)
        if not table[end][target]:
            table[end][target] = self.subsetTarget(nums, end-1, target, table)

        return table[end][target]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        table = [{} for _ in nums]
        return self.subsetTarget(nums, len(nums)-1, total//2, table)
