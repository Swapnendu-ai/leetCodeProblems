# https://leetcode.com/problems/sliding-window-maximum/submissions/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]

        heap = [(-num, idx) for idx, num in enumerate(nums[:k])]
        heapify(heap)
        start = 0
        end = k
        maxArr = []
        while end <= len(nums):
            maxVal, idx = heap[0]
            while idx < start:
                heappop(heap)
                maxVal, idx = heap[0]
            maxArr.append(-maxVal)
            if end != len(nums):
                heappush(heap, (-nums[end], end))
            end += 1
            start += 1

        return maxArr
