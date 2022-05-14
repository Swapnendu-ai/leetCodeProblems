# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y),
        }

        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operands[token](num1, num2))
                print(stack[-1], token)

        return stack.pop()
