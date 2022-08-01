# https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def swap(self, nums, i, j):
        tmp = nums[j]
        nums[j] = nums[i]
        nums[i] = tmp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start1 = start2 = -1

        for sortedTill in range(len(nums)):
            if nums[sortedTill] == 0:
                swapWith = sortedTill
                if start2 != -1:
                    self.swap(nums, swapWith, start2)
                    swapWith = start2
                    if nums[start2+1] == 2:
                        start2 += 1
                    else:
                        start2 = -1

                if start1 != -1:
                    self.swap(nums, swapWith, start1)
                    if nums[start1+1] == 1:
                        start1 += 1
                    else:
                        start1 = -1

            elif nums[sortedTill] == 1:
                if start2 != -1:
                    self.swap(nums, sortedTill, start2)
                    if start1 == -1:
                        start1 = start2
                    if nums[start2+1] == 2:
                        start2 += 1
                    else:
                        start2 = -1
                if start1 == -1:
                    start1 = sortedTill

            elif start2 == -1:
                start2 = sortedTill

            # print(sortedTill,start1,start2,nums)

        return nums
