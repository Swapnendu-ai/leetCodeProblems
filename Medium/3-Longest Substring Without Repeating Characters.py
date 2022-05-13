#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen = defaultdict(lambda: -1)
        subStringStart = 0
        maxLen = min(1,len(s))
        
        for index,c in enumerate(s):
            if lastSeen[c] >= subStringStart:
                maxLen = max(maxLen,index-subStringStart)
                subStringStart = lastSeen[c]+1
            lastSeen[c] = index
            
        return max(maxLen,len(s)-subStringStart)