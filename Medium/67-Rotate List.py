# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return (head, int(head is not None))

        prevNode = head
        curNode = head.next
        nextNode = curNode.next
        count = 2
        while nextNode is not None:
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            nextNode = curNode.next
            count += 1

        curNode.next = prevNode
        head.next = None
        return (curNode, count)

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        head, length = self.reverse(head)
        k = k % length
        if k == 0:
            return self.reverse(head)[0]

        curNode = head
        while k > 1:
            k -= 1
            curNode = curNode.next
            if curNode is None:
                curNode = head

        start = curNode
        nextNode = curNode.next

        head, _ = self.reverse(head)
        if nextNode is not None:
            nextNode.next = None
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next = head

        return start
