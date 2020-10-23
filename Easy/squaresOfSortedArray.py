# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

# The nlogn solution is very tidy. I think an O(n) solution exists for this
# problem.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x**2,A)))
