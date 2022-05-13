# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getPivot(nums, start, end):
            if end - start <= 2:
                for i in range(max(1, start), end):
                    if nums[i-1] > nums[i]:
                        return i
                return 0

            mid = start + (end-start) // 2
            if mid != 0 and nums[mid-1] > nums[mid]:
                return mid
            if nums[mid] < nums[start]:
                return getPivot(nums, start, mid)
            return getPivot(nums, mid, end)

        pivot = getPivot(nums, 0, len(nums))
        #print(pivot)

        def searchHelper(nums):
            if len(nums) <= 2:
                for index, value in enumerate(nums):
                    #print('i',index,value)
                    if target == value:
                        return index

                return -1
            mid = len(nums)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return searchHelper(nums[:mid])
            rightSearch = searchHelper(nums[mid:])
            if rightSearch != -1:
                return mid + rightSearch
            return -1

        leftSearch = searchHelper(nums[:pivot])
        if leftSearch == -1:
            rightSearch = searchHelper(nums[pivot:])
            #print('r',rightSearch)
            if rightSearch != -1:
                return pivot + rightSearch
            return -1
        return leftSearch
