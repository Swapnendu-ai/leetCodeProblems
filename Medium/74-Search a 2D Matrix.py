# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rowSearch(row):
            if len(row) <= 2:
                return target in row
            mid = len(row)//2
            if row[mid] == target:
                return True
            if target < row[mid]:
                return rowSearch(row[:mid])
            return rowSearch(row[mid+1:])
        
        if len(matrix) < 2:            
            for row in matrix:
                if row[0] <= target <= row[-1] and rowSearch(row):
                    return True
            return False
        
        mid = len(matrix) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            return rowSearch(matrix[mid])
        if target < matrix[mid][0]:
            return self.searchMatrix(matrix[:mid],target)
        return self.searchMatrix(matrix[mid+1:],target)