# https://leetcode.com/explore/featured/card/google/67/sql-2/3044/

from typing import List


class Solution:
    def convert(self, email : str) -> str:
        result = []
        stopFlag = False
        localEnd = False
        for c in email:
            if not localEnd:
                if c != '.':
                    if c == '+':
                        stopFlag = True
                    elif c == '@':
                        localEnd = True
                        result.append(c)
                    elif not stopFlag:
                        result.append(c)
            else:
                result.append(c)
        return ''.join(result)

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set(map(self.convert,emails)))
