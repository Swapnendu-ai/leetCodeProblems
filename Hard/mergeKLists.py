# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fromMyList(l):
    if len(l) == 0:
        return None

    result = ListNode(l[0])
    result.next = fromMyList(l[1:])
    return result

def toMyList(l:ListNode) -> List[int]:
    result = []
    while l is not None:
        result.append(l.val)
        l = l.next
    return result


    class Solution:
        def binaryMerge(self,list1, list2):
            if list1 is None:
                return list2
            elif list2 is None:
                return list1

            if list1.val <= list2.val:
                head = list1
                current = list1
                list1 = list1.next
            else:
                head = list2
                current = list2
                list2 = list2.next

            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next

            while list1 is not None:
                current.next = list1
                list1 = list1.next
                current = current.next

            while list2 is not None:
                current.next = list2
                list2 = list2.next
                current = current.next
            return head


        def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            if len(lists) == 0:
                return None
            if len(lists) == 1:
                return lists[0]

            partialResult = []
            if len(lists) % 2 == 0:
                for i in range(0,len(lists),2):
                    partialResult.append(self.binaryMerge(lists[i],lists[i+1]))
                    # print("even",list(map(toMyList,partialResult)))

                return self.mergeKLists(partialResult)
            else:
                for i in range(0,len(lists)-1,2):
                    partialResult.append(self.binaryMerge(lists[i],lists[i+1]))
                    # print("odd",list(map(toMyList,partialResult)))
                partialResult.append(lists[-1])
                return self.mergeKLists(partialResult)



print(toMyList(Solution().mergeKLists([fromMyList(x) for x in [[1,4,5],[1,3,4],[2,6]]])))
# print(toMyList(fromMyList([1,2,4,5])))
