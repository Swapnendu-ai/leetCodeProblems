# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rightPointer = len(numbers)-1
        
        for leftPointer, leftNumber in enumerate(numbers):
            requiredRightNumber = target - leftNumber
            while numbers[rightPointer] > requiredRightNumber:
                #print(leftPointer,rightPointer,leftNumber,numbers[rightPointer])
                rightPointer -= 1
            if numbers[rightPointer] == requiredRightNumber:
                return [leftPointer+1,rightPointer+1]