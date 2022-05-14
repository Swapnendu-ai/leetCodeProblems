# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(root,minVal,maxVal):
            if root is None:
                return True
            
            return ((minVal is None or minVal<root.val) and 
        (maxVal is None or root.val <maxVal) and 
        isValidBSTHelper(root.left,minVal,root.val) and 
        isValidBSTHelper(root.right,root.val,maxVal))
        
        return (isValidBSTHelper(root.left,None,root.val) and 
                isValidBSTHelper(root.right,root.val,None))
                