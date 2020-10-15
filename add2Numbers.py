# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fromList(l) -> ListNode:
    answer  = None
    while l:
        item = l.pop()
        newAnswer = ListNode(item,answer)
        answer = newAnswer
    return answer

def toList(l:ListNode) -> List:
    answer = []
    while l is not None:
        answer.append(l.val)
        l = l.next
    return answer


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        answer = ListNode()
        curNode = answer
        carry = 0

        while l1 is not None and l2 is not None:
            summation = l1.val + l2.val + carry
            curNode.next = ListNode(val = summation % 10)
            carry = summation // 10
            curNode = curNode.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            summation = l1.val + carry
            curNode.next = ListNode(val = summation % 10)
            carry = summation // 10
            curNode = curNode.next
            l1 = l1.next

        while l2 is not None:
            summation = l2.val + carry
            curNode.next = ListNode(val = summation % 10)
            carry = summation // 10
            curNode = curNode.next
            l2 = l2.next

        if carry == 1:
            curNode.next = ListNode(val=carry)

        return answer.next

s= Solution()


print(toList(s.addTwoNumbers(fromList([2,4,3]),fromList([5,6,4]))))
print(toList(s.addTwoNumbers(fromList([2,4,9]),fromList([5,6,4,9]))))
print(toList(s.addTwoNumbers(fromList([0]),fromList([0]))))
print(toList(s.addTwoNumbers(fromList([9,9,9,9,9,9,9]),fromList([9,9,9,9]))))
