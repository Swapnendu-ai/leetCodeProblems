# https://leetcode.com/problems/maximum-subarray/


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        partialSum = minVal = result = nums[0]
        for num in nums[1:]:
            newPartialSum = partialSum + num
            newMinVal = min(minVal,newPartialSum)
            result = max(result,newPartialSum,newPartialSum - minVal)
            partialSum = newPartialSum
            minVal = newMinVal

        return result

s = Solution()
print(s.maxSubArray([1]))
