# https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParenthesisHelper(opened=0, remaining=n):
            if remaining == 0:
                return [''.join([')']*opened)]
            if opened == 0:
                return [f'({suffix}' for suffix in generateParenthesisHelper(1, remaining-1)]
            return ([f'({suffix}' for suffix in generateParenthesisHelper(opened+1, remaining-1)] +
                    [f'){suffix}' for suffix in generateParenthesisHelper(opened-1, remaining)])

        return generateParenthesisHelper()
