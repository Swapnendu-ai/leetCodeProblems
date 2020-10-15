# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    #add the neighbors to the queue
    def addNeighbor(self,row,col):
        if (0 <= row < self.numRows
        and 0 <= col < self.numCols
        and self.grid[row][col] == '1'
        and not self.visited[row][col]):
            self.queue.append((row,col))


    def emptyQueue(self):
        while self.queue:
            row,col = self.queue.pop()
            self.visited[row][col] = True
            self.addNeighbor(row+1,col)
            self.addNeighbor(row-1,col)
            self.addNeighbor(row,col+1)
            self.addNeighbor(row,col-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.queue = []
        numIslands = 0
        self.grid = grid
        self.numRows = len(grid)
        self.numCols = len(grid[0])
        self.visited = [[False for _ in range(self.numCols)] for _ in range(self.numRows)]
        for rowNum in range(self.numRows):
            for colNum in range(self.numCols):
                if not self.visited[rowNum][colNum] and self.grid[rowNum][colNum] == '1':
                    numIslands += 1
                    self.queue.append((rowNum,colNum))
                    self.emptyQueue()
        return numIslands

s = Solution()
print(s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
print(s.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
