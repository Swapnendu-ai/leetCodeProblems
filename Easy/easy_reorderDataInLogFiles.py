#https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List


class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # def myCompare(log1,log2):
        #     if log1[1].isdigit():
        #         return 0 if log2[1].isdigit() else 1
        #     if log2[1].isdigit():
        #         return -1

        #     i = 1
        #     while i < min(len(log1),len(log2)):
        #         if log1[i] < log2[i]:
        #             return -1
        #         elif log1[i] == log2[i]:
        #             i += 1
        #         else:
        #             return 1

        #     if len(log1) == len(log2):
        #         return -1 if log1[0] < log2[0] else 0 if log1[0] == log2[0] else 1

        #     return -1 if len(log1) < len(log2) else 1



        splitLogs = map(lambda x: x.split(" "), logs)
        charLogs = []
        digitLogs = []
        for log in splitLogs:
            if log[1].isdigit():
                digitLogs.append(log)
            else:
                charLogs.append(log)
        charLogs.sort(key= lambda x: " ".join(x[1:]) + " " + x[0])
        # print(digitLogs,charLogs)

        result = list(map(lambda x: " ".join(x),charLogs))
        result.extend(map(lambda x: " ".join(x),digitLogs))
        return result

s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

#actual solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)
