# https://leetcode.com/problems/reverse-bits/submissions/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for bit in range(32):
            result = (result << 1) + (n & 1)
            n = n >> 1

        return result
