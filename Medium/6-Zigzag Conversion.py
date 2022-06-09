# https://leetcode.com/problems/zigzag-conversion/submissions/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lines = [[] for _ in range(numRows)]

        line = 0
        enterOne = False

        for c in s:
            lines[line].append(c)
            if line == 0:
                enterOne = False
            if line == numRows-1:
                enterOne = True
            if enterOne:
                line -= 1
            else:
                line += 1

        result = []
        #print(lines)
        for line in lines:
            result.extend(line)

        return ''.join(result)
