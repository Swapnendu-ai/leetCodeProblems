# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0]*n

        def climbStairsHelper(n):
            if n <= 2:
                return n
            if table[n-1]:
                return table[n-1]
            table[n-1] = climbStairsHelper(n-1) + climbStairsHelper(n-2)
            return table[n-1]

        return climbStairsHelper(n)
