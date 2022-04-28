#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        answer = ListNode() #head to be removed
        head = answer
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + carry
            head.next = ListNode(val = sum %10)
            carry = sum//10
            head = head.next
            l1 = l1.next
            l2 = l2.next
            
        while l1 is not None:
            sum = l1.val  + carry
            head.next = ListNode(val = sum %10)
            carry = sum//10
            head = head.next
            l1 = l1.next
            
        while l2 is not None:
            sum = l2.val  + carry
            head.next = ListNode(val = sum %10)
            carry = sum//10
            head = head.next
            l2 = l2.next
            
        if carry > 0:
            head.next = ListNode(val = carry)
            
        return answer.next
            
        