# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        nextNode = head.next
        head.next = None
        prevNode = head
        while nextNode is not None:
            curNode = nextNode
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode

        return prevNode
