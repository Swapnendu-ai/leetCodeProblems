# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/

class Solution:
    def DFS(self, row, col, matrix, table):
        if table[row][col] is not None:
            return table[row][col]

        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        maxPathSize = 0
        for nextRow, nextCol in neighbors:
            if (
                0 <= nextRow < len(matrix) and
                0 <= nextCol < len(matrix[0]) and
                matrix[row][col] < matrix[nextRow][nextCol]
            ):
                maxPathSize = max(
                    maxPathSize,
                    self.DFS(nextRow, nextCol, matrix, table),
                )

        table[row][col] = maxPathSize + 1
        return maxPathSize + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0

        table = [[None]*len(matrix[0]) for _ in matrix]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                self.DFS(row, col, matrix, table)

        maxSize = 0
        for row in range(len(table)):
            for col in range(len(table[row])):
                maxSize = max(maxSize, table[row][col])

        return maxSize
