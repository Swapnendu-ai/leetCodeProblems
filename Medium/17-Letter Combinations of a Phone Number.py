# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

class Solution:
    def __init__(self):
        self.map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) > 1:
            suffix = self.letterCombinations(digits[1:])
        else:
            return self.map[digits[0]]

        result = []
        for char in self.map[digits[0]]:
            for suf in suffix:
                result.append(char+suf)

        return result
