#https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    smaller = None
    def generateParenthesis(self, n: int) -> List[str]:
        def create(child:str):
            return [wrapChild(child),'()'+child,child+'()']

        def wrapChild(child:str):
            return '(' + child + ')'

        if n == 1:
            self.smaller = ['()']
            return ['()']
        if n%2 == 0:
            children = self.generateParenthesis(n-1)
            modified = map(create,children)
            self.smaller = list(set(child for childList in modified for child in childList)
                                | set(map(wrapChild,self.smaller)))
            return self.smaller
        else:
            children = self.generateParenthesis(n-1)
            modified = map(create,children)
            return list(set(child for childList in modified for child in childList))


