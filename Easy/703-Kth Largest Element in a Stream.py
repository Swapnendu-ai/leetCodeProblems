# https://leetcode.com/problems/kth-largest-element-in-a-stream/submissions/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = sorted(nums, reverse=True)[:k]
        heapify(self.minHeap)
        self.k = k

    def add(self, val: int) -> int:
        #print(self.minHeap)
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
            return self.minHeap[0]
        if val > self.minHeap[0]:
            heappop(self.minHeap)
            heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
