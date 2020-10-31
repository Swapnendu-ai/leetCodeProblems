# https://leetcode.com/problems/fixed-point/

from typing import List


class Solution:
    def fixedPointHelper(self,A,adjustment):
        print(A,adjustment)
        if not A:
            return -1
        if len(A) == 1:
            return adjustment if A[0] == adjustment else -1

        mid = len(A) // 2

        if mid + adjustment == A[mid]:
            result = self.fixedPointHelper(A[:mid],adjustment)
            if result == -1:
                return mid + adjustment
            else:
                return result
        if mid + adjustment > A[mid]:
            return self.fixedPointHelper(A[mid+1:],mid + adjustment + 1)
        else:
            return self.fixedPointHelper(A[:mid],adjustment)

    def fixedPoint(self, A: List[int]) -> int:
        # return self.fixedPointHelper(A,0)
        for i, v in enumerate(A):
            if i == v:
                return i
        return -1

