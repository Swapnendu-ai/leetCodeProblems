# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            start = list1
            list1 = list1.next
        else:
            start = list2
            list2 = list2.next
        head = start
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.next = list1
                head = list1
                list1 = list1.next
            else:
                head.next = list2
                head = list2
                list2 = list2.next

        if list1 is not None:
            head.next = list1

        if list2 is not None:
            head.next = list2

        return start
