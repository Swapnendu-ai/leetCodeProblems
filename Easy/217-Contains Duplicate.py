# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbersSeen = set()
        for num in nums:
            if num in numbersSeen:
                return True
            numbersSeen.add(num)
        return False
