# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.leftHeap = []
        self.rightHeap = []

    def leftHeapAdd(self, num):
        heappush(self.leftHeap, -num)

    def leftHeapPop(self):
        return -heappop(self.leftHeap)

    def rightHeapAdd(self, num):
        heappush(self.rightHeap, num)

    def rebalance(self):
        while abs(len(self.leftHeap) - len(self.rightHeap)) > 1:
            if len(self.leftHeap) > len(self.rightHeap):
                self.rightHeapAdd(self.leftHeapPop())
            else:
                self.leftHeapAdd(heappop(self.rightHeap))

    def addNum(self, num: int) -> None:
        if len(self.rightHeap) == 0 or num < self.rightHeap[0]:
            self.leftHeapAdd(num)
        else:
            self.rightHeapAdd(num)

        self.rebalance()

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (self.rightHeap[0]-self.leftHeap[0]) / 2.0
        elif len(self.leftHeap) > len(self.rightHeap):
            return -self.leftHeap[0]
        else:
            return self.rightHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
