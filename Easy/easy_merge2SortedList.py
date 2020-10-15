# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        result = ListNode()
        currNode = result
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                currNode.next = l1
                currNode = currNode.next
                l1 = l1.next
            else:
                currNode.next = l2
                currNode = currNode.next
                l2 = l2.next
        while l1 is not None:
            currNode.next = l1
            currNode = currNode.next
            l1 = l1.next

        while l2 is not None:
            currNode.next = l2
            currNode = currNode.next
            l2 = l2.next

        return result.next


