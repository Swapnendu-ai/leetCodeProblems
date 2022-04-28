# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

        for letter in t:
            if letter in letters and letters[letter] > 0:
                letters[letter] -= 1
            else:
                return False

        return sum(letters.values()) == 0
