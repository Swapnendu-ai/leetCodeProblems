# https://leetcode.com/problems/happy-number/submissions/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            seen.add(n)
            sumDigits = 0
            while n > 0:
                sumDigits += (n % 10)**2
                n = n//10

            if sumDigits == 1:
                return True
            n = sumDigits
