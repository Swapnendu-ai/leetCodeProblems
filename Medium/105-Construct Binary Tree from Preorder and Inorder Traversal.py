# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeHelper(self, preorder: List[int], preOrderIndex, inorder: List[int]):
        if len(inorder) == 0:
            return (None,preOrderIndex-1)
        
        # print(preOrderIndex,inorder)
        root = TreeNode(preorder[preOrderIndex])
        less, more = [], []
        switch = False
        for num in inorder:
            if num == preorder[preOrderIndex]:
                switch = True
            elif not switch:
                less.append(num)
            else:
                more.append(num)
                
        root.left, preOrderIndex = self.buildTreeHelper(preorder,preOrderIndex+1,less)
        root.right, preOrderIndex = self.buildTreeHelper(preorder,preOrderIndex+1,more)
        
        return (root,preOrderIndex)
        
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder,0,inorder)[0]