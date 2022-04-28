from collections import defaultdict
class Solution:

    def getNextIndex(self,start:int,getLarger : bool) -> int:
        if getLarger:
            value = self.A[-1]
            index = len(self.A) -1
            for i, c in enumerate(self.A[start+1:]):
                if c < value and c >= self.A[start]:
                    value = c
                    index = 1+i+start
            print("h",start,index,value)
            return index if value >= self.A[start] else None
        else:
            value = self.A[start+1]
            index = start+1
            for i, c in enumerate(self.A[start+1:]):
                if c > value and c <= self.A[start]:
                    value = c
                    index = 1+i+start
            return index if value <= self.A[start] else None


    def search(self,start:int,isEvenJump:bool) -> None:
        print(start,isEvenJump)
        if start is None:
            return False
        if isEvenJump in self.dp[start]:
            return self.dp[start][isEvenJump]

        self.dp[start][isEvenJump] = self.search(self.getNextIndex(start,isEvenJump),not isEvenJump)
        return self.dp[start][isEvenJump]

    def oddEvenJumps(self, A: List[int]) -> int:
        self.A = A
        self.dp = [defaultdict(lambda : False) for _ in A]
        self.dp[-1] = {True:True,False:True}
        for i in range(0,len(self.A)):
            self.search(i,isEvenJump = True)
        print([(x[True],x[False]) for x in self.dp])
        return sum(map(lambda x : x[True] or x[False],self.dp))
        