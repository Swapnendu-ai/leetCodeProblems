# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesHelper(root,maxVal):
            if root is None:
                return 0
            return int(root.val >= maxVal) + goodNodesHelper(root.left,max(maxVal,root.val)) + goodNodesHelper(root.right,max(maxVal,root.val))
        
        return 1 + goodNodesHelper(root.left,root.val) + goodNodesHelper(root.right,root.val)