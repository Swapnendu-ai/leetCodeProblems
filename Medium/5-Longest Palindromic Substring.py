# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        isPalindromeTable = [[True]*len(s)]+[[None]*len(s)
                                             for _ in range(len(s)-1)]

        result = (0, 1)
        for maxLen in range(2, len(s)+1):
            for start in range(len(s)-maxLen, -1, -1):
                isPalindromeTable[maxLen-1][start] = (
                    s[start] == s[start+maxLen-1] and (
                        (maxLen >= 3 and isPalindromeTable[maxLen-3][start+1]) or
                        maxLen < 3
                    )
                )
                if isPalindromeTable[maxLen-1][start]:
                    result = (start, maxLen)

        return s[result[0]:result[0]+result[1]]
