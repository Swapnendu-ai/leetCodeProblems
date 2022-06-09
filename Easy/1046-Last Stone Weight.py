# https://leetcode.com/problems/last-stone-weight/submissions/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            stone1 = -heappop(heap)
            stone2 = -heappop(heap)
            if stone1 != stone2:
                heappush(heap, -abs(stone1-stone2))
            #print(heap)

        return 0 if len(heap) == 0 else -heap[0]
