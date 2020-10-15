# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        xCopy = x
        while xCopy >0:
            reverse = reverse*10 + xCopy%10
            xCopy //= 10
        return reverse == x

testCases = [121,-121,10,0,-10]
for i in testCases:
    print(Solution().isPalindrome(i))

