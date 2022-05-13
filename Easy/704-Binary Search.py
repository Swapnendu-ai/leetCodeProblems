# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            for index, item in enumerate(nums):
                if item == target:
                    return index
            return -1

        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        searchResult = self.search(nums[mid:], target)
        if searchResult == -1:
            return -1
        return mid + searchResult
