# https://leetcode.com/problems/set-matrix-zeroes/submissions/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow, zeroCol = set(), set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeroRow.add(row)
                    zeroCol.add(col)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zeroRow or col in zeroCol:
                    matrix[row][col] = 0
