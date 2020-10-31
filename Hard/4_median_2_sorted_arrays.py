# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def split(self, L, target):
        start = 0
        end = len(L)

        if not end:
            return end

        while end - start > 1:
            mid = (start + end) // 2
            if L[mid] == target:
                return mid
            elif L[mid] < target:
                start = mid
            else:
                end = mid

        return start if target <= L[start] else end

    def getElemIn(self, curList, otherList, numElemLeft):
        start = 0
        end = len(curList)

        while start < end:
            mid = (start + end) // 2
            elemLeft = self.split(otherList, curList[mid])
            totalElemLeft = elemLeft + mid
            if (totalElemLeft == numElemLeft
                or (elemLeft < len(otherList)
                    and otherList[elemLeft] == curList[mid]
                    and totalElemLeft + 1 == numElemLeft)):
                return curList[mid]
            elif totalElemLeft < numElemLeft:
                if start == mid:
                    return
                start = mid
            else:
                end = mid

    def getElem(self, numElemLeft):
        elem = self.getElemIn(self.L, self.R, numElemLeft)
        if elem is None:
            return self.getElemIn(self.R, self.L, numElemLeft)
        return elem

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.L = nums1
        self.R = nums2

        half = (len(self.L) + len(self.R)) // 2
        if (len(self.L) + len(self.R)) % 2 == 0:
            return (self.getElem(half-1) + self.getElem(half)) / 2
        else:
            return self.getElem(half)


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
print(Solution().findMedianSortedArrays([0, 0], [0, 0]))
print(Solution().findMedianSortedArrays([], [1]))
print(Solution().findMedianSortedArrays([2], []))
print(Solution().findMedianSortedArrays([2], [2]))
print(Solution().findMedianSortedArrays([2, 2], [2]))
