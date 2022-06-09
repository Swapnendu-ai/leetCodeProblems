# https://leetcode.com/problems/word-break/submissions/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memoizationTable = [None] * len(s)

        def wordBreakHelper(startIndex):
            if startIndex >= len(s):
                return True
            if memoizationTable[startIndex] is not None:
                return memoizationTable[startIndex]

            for word in wordDict:
                memoizationTable[startIndex] = (
                    s[startIndex:].startswith(word) and
                    wordBreakHelper(startIndex+len(word))
                )
                if memoizationTable[startIndex]:
                    return True

        return wordBreakHelper(0)
