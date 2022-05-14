# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c in paran:
                stack.append(c)
            else:
                if not stack or not paran[stack.pop()] == c:
                    return False

        return len(stack) == 0
