# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthSmallestHelper(root,k):
            if root is None:
                # (value if exists, size of tree)
                return (None,0)
            
            leftVal = kthSmallestHelper(root.left,k)
            if leftVal[0] is not None:
                return leftVal
            if leftVal[1] == k-1:
                return (root.val,None)
            rightVal = kthSmallestHelper(root.right,k-1-leftVal[1])
            if rightVal[0] is not None:
                return rightVal
            return (None,leftVal[1]+rightVal[1]+1)
        
        return kthSmallestHelper(root,k)[0]