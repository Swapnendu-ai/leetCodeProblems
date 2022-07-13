# https://leetcode.com/problems/symmetric-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqualModified(self, left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.isEqualModified(left.left,right.right) and self.isEqualModified(left.right,right.left)
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isEqualModified(root.left,root.right)