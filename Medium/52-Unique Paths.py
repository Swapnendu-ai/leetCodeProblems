# https://leetcode.com/problems/unique-paths/submissions/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numberOfPaths = [[None]*(n-1) + [1] for _ in range(m-1)] + [[1]*n]

        for row in range(m-2, -1, -1):
            for cell in range(n-2, -1, -1):
                numberOfPaths[row][cell] = numberOfPaths[row +
                                                         1][cell] + numberOfPaths[row][cell+1]

        return numberOfPaths[0][0]
