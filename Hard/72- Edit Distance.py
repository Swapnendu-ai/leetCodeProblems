# https://leetcode.com/problems/edit-distance/submissions/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        table = [[None]*len(word2) for _ in word1]

        def minDistanceHelper(word1End, word2End):
            #print(word1End,word2End)
            if table[word1End][word2End] is not None:
                return table[word1End][word2End]
            if word1End == 0 and word2End == 0:
                table[word1End][word2End] = int(word1[0] != word2[0])
                return table[word1End][word2End]
            if word1End == 0:
                table[word1End][word2End] = word2End+1 - \
                    int(word1[word1End] in word2[:word2End+1])
                return table[word1End][word2End]
            if word2End == 0:
                table[word1End][word2End] = word1End+1 - \
                    int(word2[word2End] in word1[:word1End+1])
                return table[word1End][word2End]
            if word1[word1End] == word2[word2End]:
                table[word1End][word2End] = minDistanceHelper(
                    word1End-1, word2End-1)
                return table[word1End][word2End]
            else:
                table[word1End][word2End] = 1 + min(
                    minDistanceHelper(word1End-1, word2End-1),
                    minDistanceHelper(word1End, word2End-1),
                    minDistanceHelper(word1End-1, word2End)
                )
                #print(table)
                return table[word1End][word2End]

        val = minDistanceHelper(len(word1)-1, len(word2)-1)
        # for i, row in enumerate(table):
        #     print(i+1,row)
        return val
