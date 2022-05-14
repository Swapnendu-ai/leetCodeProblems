# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        headCopy = head
        while headCopy is not None:
            size += 1
            headCopy = headCopy.next
        n = size - n + 1
        if n == 1:
            return head.next
        headCopy = head
        count = 0
        while True:
            count += 1
            #print(count,headCopy.val,n)
            if count == n-1:
                headCopy.next = headCopy.next.next
                return head
            headCopy = headCopy.next
