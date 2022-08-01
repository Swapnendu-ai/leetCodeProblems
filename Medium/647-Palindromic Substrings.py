# https://leetcode.com/problems/palindromic-substrings/submissions/

class Solution:
    def countSubstrings(self, s: str) -> int:
        isPalTable = [[True]*len(s)] + [[False]*len(s)
                                        for _ in range(1, len(s))]
        # subString =  [[1]*len(s)] + [[None]*len(s) for _ in range(1,len(s))]

        for length in range(2, len(s)+1):
            for start in range(0, len(s)-length+1):
                isPalTable[length-1][start] = (
                    s[start] == s[start+length-1] and
                    (isPalTable[length-3][start+1] or length == 2)
                )

        # print(isPalTable)
        return sum(sum(row) for row in isPalTable)
