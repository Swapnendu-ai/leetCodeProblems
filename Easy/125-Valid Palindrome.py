# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedChars = [c.lower() for c in s if c.isalnum()]

        for i in range(0, len(cleanedChars)//2):
            if cleanedChars[i] != cleanedChars[len(cleanedChars)-i-1]:
                return False

        return True

