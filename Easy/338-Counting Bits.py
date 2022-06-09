# https://leetcode.com/problems/counting-bits/submissions/

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        nextPowerOf2 = 1
        prevPowerOf2 = 1

        for index in range(1, n+1):
            if index == nextPowerOf2:
                result[index] = 1
                prevPowerOf2 = nextPowerOf2
                nextPowerOf2 *= 2
            else:
                result[index] = 1 + result[index-prevPowerOf2]

        return result
