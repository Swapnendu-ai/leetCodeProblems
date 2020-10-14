#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '{':'}',
            '[':']',
            '(':')',
        }
        for bracket in s:
            if bracket in {'{','[','('}:
                stack.append(bracket)
            elif not (stack and match[stack.pop()] == bracket):
                return False
        return len(stack) == 0

