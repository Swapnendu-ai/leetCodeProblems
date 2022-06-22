# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        nextNode = cur.next
        while nextNode is not None:
            if nextNode.val == cur.val:
                cur.next = nextNode.next
            else:
                cur = cur.next
            nextNode = cur.next
        return head
