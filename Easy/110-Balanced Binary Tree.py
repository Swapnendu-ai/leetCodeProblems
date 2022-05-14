# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedHelper(root):
            if root is None:
                # (isBalanced, height)
                return (True, 0)

            leftVal = isBalancedHelper(root.left)
            rightVal = isBalancedHelper(root.right)

            return (
                leftVal[0] and rightVal[0] and abs(
                    leftVal[1]-rightVal[1]) <= 1,
                1 + max(leftVal[1], rightVal[1])
            )

        return isBalancedHelper(root)[0]

