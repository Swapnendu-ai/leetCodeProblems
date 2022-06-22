# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        idx = len(s) - 1
        wordSeen = False

        while idx >= 0 and s[idx] != ' ' or not wordSeen:
            if s[idx] != ' ':
                wordSeen = True
            count += wordSeen
            idx -= 1

        return count
