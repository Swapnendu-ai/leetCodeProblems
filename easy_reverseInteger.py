#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            result = -int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])
        if result < -2**31 or result >= 2**31:
            return 0
        else:
            return result

s = Solution()
print(s.reverse(-127382769))
print(s.reverse(127382769))
