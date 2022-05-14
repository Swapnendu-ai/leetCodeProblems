# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toList(self, head):
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        return l

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        size = 0
        headCopy = head
        while headCopy is not None:
            size += 1
            headCopy = headCopy.next

        def reverse(head):
            if head is None or head.next is None:
                return head
            reversedList = reverse(head.next)
            head.next.next = head
            head.next = None
            return reversedList

        headCopy = head
        count = 0
        while count < floor(size/2) - ((size+1) % 2):
            count += 1
            headCopy = headCopy.next

        #print(self.toList(headCopy))
        reversedList = reverse(headCopy.next)
        headCopy.next = None
        #print(self.toList(reversedList))
        #print(self.toList(head))
        headCopy = head

        while headCopy is not None and reversedList is not None:
            nextNode = headCopy.next
            headCopy.next = reversedList
            reversedList = reversedList.next
            headCopy.next.next = nextNode
            headCopy = nextNode
