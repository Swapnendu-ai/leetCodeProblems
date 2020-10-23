# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def swap(index1:int, index2:int,nums1: List[int],nums2: List[int]) -> int:
            temp = nums2[index2]
            nums2[index2] = nums1[index1]
            nums1[index1] = temp

        index1 = 0
        while index1<m and len(nums2):
            if nums1[index1] <= nums2[0]:
                index1 += 1
            else:
                swap(index1,0,nums1,nums2)
                index1 += 1
                index2 = 0
                while index2 + 1 !=n and nums2[index2] > nums2[index2+1]:
                    swap(index2,index2+1,nums2,nums2)
                    index2 += 1

        for index in range(m,len(nums1)):
            nums1[index] = nums2[index-m]


