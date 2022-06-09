# https://leetcode.com/problems/target-sum/submissions/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        num = nums.pop()
        if num == 0:
            possibilities = {0: 2}
        else:
            possibilities = {num: 1, -num: 1}
        if len(nums) == 0:
            return int(target in possibilities)
        while nums:
            num = nums.pop()
            nextPossibilities = defaultdict(int)
            for possibity, count in possibilities.items():
                nextPossibilities[possibity+num] += count
                nextPossibilities[possibity-num] += count
            possibilities = nextPossibilities

        return possibilities[target]
