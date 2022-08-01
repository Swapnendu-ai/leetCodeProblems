# https://leetcode.com/problems/rotate-image/submissions/

class Solution:
    def swap(self, matrix, r1, c1, r2, c2):
        tmp = matrix[r1][c1]
        matrix[r1][c1] = matrix[r2][c2]
        matrix[r2][c2] = tmp

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row > col:
                    self.swap(matrix, row, col, col, row)

        for row in range(len(matrix)):
            matrix[row].reverse()
