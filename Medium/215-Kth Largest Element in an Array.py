# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pick = choice(nums)
        less = []
        more = []
        count = 0
        for num in nums:
            if num < pick:
                less.append(num)
            elif num > pick:
                more.append(num)
            else:
                count += 1
        
        # print(less,more,count, pick, k)
        if k <= len(more):
            return self.findKthLargest(more,k)
        if len(more) + count >= k:
            return pick
        return self.findKthLargest(less,k-len(more)-count)