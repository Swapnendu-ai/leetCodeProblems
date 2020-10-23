# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <=1:
            return len(s)

        lastRepeatedPosition = -1
        lastSeen = defaultdict(lambda : -1)
        maxSubString = 1
        lastSeen[s[0]] = 0

        for index, character in enumerate(s):
            if index:
                sizeThisSubString = index - max(lastSeen[character],lastRepeatedPosition)
                if sizeThisSubString > maxSubString:
                    maxSubString = sizeThisSubString

                lastRepeatedPosition = max(lastRepeatedPosition,lastSeen[character])
                lastSeen[character] = index

        return maxSubString

