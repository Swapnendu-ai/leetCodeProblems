# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        for rowNum in range(len(grid)):
            for colNum in range(len(grid[rowNum])):
                curSize = 0
                stack = [(rowNum, colNum)]
                while stack:
                    curRowNum, curColNum = stack.pop()
                    if 0 <= curRowNum < len(grid) and 0 <= curColNum < len(grid[rowNum]) and grid[curRowNum][curColNum] == 1:
                        curSize += 1
                        grid[curRowNum][curColNum] = -1
                        stack.extend([(curRowNum-1, curColNum), (curRowNum+1, curColNum),
                                     (curRowNum, curColNum-1), (curRowNum, curColNum+1)])

                maxSize = max(curSize, maxSize)

        return maxSize
