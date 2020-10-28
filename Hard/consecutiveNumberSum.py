# https://leetcode.com/problems/consecutive-numbers-sum/

#O(N) solution
class Solution:
    class SlidingWindow:
        def __init__(self,lo,hi):
            self.lo = lo
            self.hi = hi

        def sum(self):
            return (self.hi-self.lo + 1)*(self.hi+self.lo)/2

        def increase(self):
            self.lo -= 1

        def move(self):
            self.lo -= 1
            self.hi -= 1

    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        if N %2 :
            sw = self.SlidingWindow(N//2,N//2+1)
        else:
            sw = self.SlidingWindow(N//2-1,N//2+1)

        while sw.lo > 0:
            windowSum = sw.sum()
            if windowSum == N:
                count += 1
                sw.move()
            elif windowSum < N:
                sw.increase()
            else:
                sw.move()

        return count
