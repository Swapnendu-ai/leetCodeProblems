# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestCommonAncestorHelper(root):
            if root is None:
                # (isPdecendant, isQdecendant,LCA if exits)
                return (False, False, None)
            leftVal = lowestCommonAncestorHelper(root.left)
            #print('l',leftVal)
            if leftVal[0] and leftVal[1]:
                return leftVal
            rightVal = lowestCommonAncestorHelper(root.right)
            #print('r',rightVal)
            if rightVal[0] and rightVal[1]:
                return rightVal
            if (leftVal[0] or root.val == p.val) and (rightVal[1] or root.val == q.val):
                #print('l1',root)
                return (True, True, root)
            if (leftVal[1] or root.val == q.val) and (rightVal[0] or root.val == p.val):
                return (True, True, root)
            return (
                leftVal[0] or rightVal[0] or root.val == p.val,
                leftVal[1] or rightVal[1] or root.val == q.val,
                None
            )

        return lowestCommonAncestorHelper(root)[2]
