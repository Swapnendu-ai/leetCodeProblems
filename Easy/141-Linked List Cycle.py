# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = hare = head
        while True:
            if turtle is None or turtle.next is None:
                return False
            else:
                turtle = turtle.next
            if hare is None or hare.next is None or hare.next.next is None:
                return False
            else:
                hare = hare.next.next
            if turtle == hare:
                return True
