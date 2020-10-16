# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def compare(dictionary,word1,word2):
            index = 0
            while index < min(len(word1),len(word2)):
                if dictionary[word1[index]] > dictionary[word2[index]]:
                    return False
                elif dictionary[word1[index]] < dictionary[word2[index]]:
                    return True
                index += 1

            return len(word1) <= len(word2)

        if len(words) <= 1:
            return True

        dictionary = {order[i] : i for i in range(len(order))}

        for i in range(1,len(words)):
            if not compare(dictionary,words[i-1],words[i]):
                return False

        return True




