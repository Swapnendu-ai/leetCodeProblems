# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        def isEqual(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            return root.val == subRoot.val and isEqual(root.left,subRoot.left) and isEqual(root.right,subRoot.right)
        
        return (root.val == subRoot.val and isEqual(root,subRoot)) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)