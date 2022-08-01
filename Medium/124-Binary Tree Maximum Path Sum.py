# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumHelper(self, root: Optional[TreeNode]):
        leftSum, leftMax, rightSum, rightMax = None, None, None, None
        if root.left is not None:
            leftSum, leftMax = self.maxPathSumHelper(root.left)
        if root.right is not None:
            rightSum, rightMax = self.maxPathSumHelper(root.right)

        if leftSum is None:
            if rightSum is None:
                return (root.val, root.val)
            else:
                maxSumSoFar = max(root.val, root.val+rightSum)
                return (
                    maxSumSoFar,
                    max(root.val, rightMax, maxSumSoFar)
                )
        else:
            if rightSum is None:
                maxSumSoFar = max(root.val, root.val+leftSum)
                return (
                    maxSumSoFar,
                    max(root.val, leftMax, maxSumSoFar))
            else:
                maxSum = max(leftSum, rightSum)
                maxSumSoFar = max(root.val, root.val+maxSum)
                return (
                    maxSumSoFar,
                    max(
                        root.val, leftMax,
                        rightMax, maxSumSoFar,
                        root.val+leftSum+rightSum
                    )
                )

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxPathSumHelper(root)[1]
