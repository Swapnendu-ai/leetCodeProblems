# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = [[root]]
        finishFlag = False

        while not finishFlag:
            nextLevel = []
            curLevelUnprocessed = result.pop()
            result.append(curLevelUnprocessed[-1].val)
            for node in curLevelUnprocessed:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)

            if not nextLevel:
                finishFlag = True
            else:
                result.append(nextLevel)
        return result
