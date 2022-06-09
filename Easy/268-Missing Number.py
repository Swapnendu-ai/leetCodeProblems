# https://leetcode.com/problems/missing-number/submissions/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missingNumber = 0

        for guess in range(0, len(nums)+1):
            missingNumber = missingNumber ^ guess

        for num in nums:
            missingNumber = missingNumber ^ num

        return missingNumber
