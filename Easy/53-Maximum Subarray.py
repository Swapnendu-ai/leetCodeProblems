# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumSoFar = None
        contiguousSums = -1

        for num in nums:
            if num < 0:
                if sumSoFar is not None:
                    contiguousSums = max(contiguousSums, sumSoFar)
                    sumSoFar = max(0, sumSoFar+num)
            elif sumSoFar is None:
                sumSoFar = num
            else:
                sumSoFar += num
            #print(sumSoFar)
        if sumSoFar is not None and sumSoFar >= 0:
            contiguousSums = max(sumSoFar, contiguousSums)

        if contiguousSums > 0:
            return contiguousSums
        return max(nums)
