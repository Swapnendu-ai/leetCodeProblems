# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head is None or head.next is None:
#             return head

#         prev = head
#         head = head.next
#         prev.next = None
#         while head is not None:
#             nextPointer = head.next
#             head.next = prev
#             prev = head
#             head = nextPointer


#         return prev

        def helper(self,head,prev):
            if head.next is None:
                head.next = prev
                return head

            reversedHead = self.helper(head.next,head)
            head.next = prev
            return reversedHead

        def reverseList(self, head: ListNode) -> ListNode:
            if head is None:
                return head

            return self.helper(head,None)
