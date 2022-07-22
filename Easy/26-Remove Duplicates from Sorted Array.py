# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = None
        insertIndex = 0
        for num in nums:
            if num != lastNum:
                nums[insertIndex] = num
                lastNum = num
                insertIndex += 1

        return insertIndex
