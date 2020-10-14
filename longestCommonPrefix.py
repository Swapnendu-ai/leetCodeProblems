#https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        if not strs:
            return ''
        for i in range(min(map(len,strs))):
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] != ch:
                    return ''.join(result)
            result.append(ch)
        return ''.join(result)
