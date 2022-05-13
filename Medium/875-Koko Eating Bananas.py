# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            return sum(ceil(p/k) for p in piles) <= h
        
        minV =1
        maxV = 1
        while not canEat(maxV):
            minV = maxV
            maxV *= 2
            
        def search(minV,maxV):
            if maxV - minV <= 2:
                for k in range(minV,maxV+1):
                    if canEat(k):
                        return k
            mid = minV + (maxV-minV)//2
            if canEat(mid):
                if canEat(mid-1):
                    return search(minV,mid)
                return mid
            return search(mid+1,maxV)
        
        return search(minV,maxV)