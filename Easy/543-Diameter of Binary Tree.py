# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameterOfBinaryTreeHelper(root):
            if root is None:
                #(diameter,maxDepth)
                return (0, 0)
            leftVal = diameterOfBinaryTreeHelper(root.left)
            rightVal = diameterOfBinaryTreeHelper(root.right)
            #print(root.val,leftVal,rightVal)
            if root.left is None:
                return (max(rightVal[0], rightVal[1]), 1+rightVal[1])
            if root.right is None:
                return (max(leftVal[0], leftVal[1]), 1+leftVal[1])
            return (max(leftVal[0], rightVal[0], leftVal[1]+rightVal[1]), 1+max(leftVal[1], rightVal[1]))

        return diameterOfBinaryTreeHelper(root)[0]
