#https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lo1, hi1 = 0, len(nums1)
        lo2, hi2 = 0, len(nums2)
        
        while lo1 < hi1 and lo2 < hi2:
            mid1 = (lo1+hi1)//2
            mid2 = (lo2+hi2)//2
            if nums1[mid1] <= nums2[mid2]:
                lo1 = mid1
                hi2 = mid2
            else:
                lo2 = mid2
                hi1 = mid1
                
            #print(lo1,hi1,lo2,hi2)
                
        if (len(nums1)+len(nums2))%2:
            return max(nums1[lo1],nums2[lo2])
        else:
            if lo1 + 1 < len(nums1) and lo2 + 1 < len(nums2):
                return (max(nums1[lo1],nums2[lo2])+ min(nums1[lo1+1],nums2[lo2+1]))/2
            elif lo1 + 1 < len(nums1):
                return (max(nums1[lo1],nums2[lo2])+ nums1[lo1+1])/2
            return (max(nums1[lo1],nums2[lo2])+ nums2[lo2+1])/2
        