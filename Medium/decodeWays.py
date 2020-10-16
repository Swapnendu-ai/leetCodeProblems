class Solution:

    def numDecodings(self, s: str) -> int:
        def inRange(num: str, throwErrorOnFail=False):
            check = 0 < int(num) < 27
            if throwErrorOnFail and not check:
                raise ValueError
            else:
                return int(check)

        try:
            if len(s) == 1:
                return inRange(s)

            self.dpTable = [inRange(s[0],throwErrorOnFail=True)]
            self.dpTable.append(
                1 + inRange(s[:2]) if inRange(s[1])
                else inRange(s[:2], throwErrorOnFail=True))

            for i in range(2, len(s)):
                if inRange(s[i]):
                    if inRange(s[i-1:i+1]) and inRange(s[i-1]):
                        self.dpTable.append(
                            self.dpTable[-1] + self.dpTable[-2])
                    else:
                        self.dpTable.append(self.dpTable[-1])
                elif inRange(s[i-1:i+1],throwErrorOnFail=True):
                    self.dpTable.append(self.dpTable[-2])

            return self.dpTable[-1]

        except ValueError:
            return 0

s = Solution()
print(s.numDecodings("10011"))
print(s.numDecodings("12"))
print(s.numDecodings("226"))
print(s.numDecodings("0"))
print(s.numDecodings("1"))
