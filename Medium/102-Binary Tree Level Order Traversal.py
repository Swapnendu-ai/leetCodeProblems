#https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = [[root]]
        finishFlag = False

        while not finishFlag:
            nextLevel = []
            curLevelUnprocessed = result.pop()
            curLevel = []
            for node in curLevelUnprocessed:
                curLevel.append(node.val)
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)

            result.append(curLevel)
            if not nextLevel:
                finishFlag = True
            else:
                result.append(nextLevel)
        return result
