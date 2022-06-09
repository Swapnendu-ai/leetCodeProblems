# https://leetcode.com/problems/decode-ways/

class Solution:
    def __init__(self):
        self.numToChar = {str(i): chr(64+i) for i in range(1, 27)}

    def numDecodings(self, s: str) -> int:
        numDecodingsTable = [None]*len(s)

        def numDecodingsHelper(start):
            if start >= len(s):
                return int(start == len(s))
            if numDecodingsTable[start] is not None:
                return numDecodingsTable[start]

            numDecodingsFromHere = 0
            if s[start] in self.numToChar:
                numDecodingsFromNext = numDecodingsHelper(start+1)
                if numDecodingsFromNext != 0:
                    numDecodingsFromHere = numDecodingsFromNext

            if s[start:start+2] in self.numToChar:
                numDecodingsFromNext = numDecodingsHelper(start+2)
                if numDecodingsFromNext != 0:
                    numDecodingsFromHere += numDecodingsFromNext

            numDecodingsTable[start] = numDecodingsFromHere
            return numDecodingsFromHere

        result = numDecodingsHelper(0)
        #print(numDecodingsTable)
        return result
