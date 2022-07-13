# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return head

        length = 0
        curNode = head
        while curNode is not None:
            length += 1
            curNode = curNode.next

        if length == 1:
            return TreeNode(val=head.val)

        median = 1 + length//2

        i = 1
        curNode = head
        while i < median-1:
            i += 1
            curNode = curNode.next

        # print(curNode.next.val)
        root = TreeNode(val=curNode.next.val)
        root.right = self.sortedListToBST(curNode.next.next)
        curNode.next = None
        root.left = self.sortedListToBST(head)

        return root
