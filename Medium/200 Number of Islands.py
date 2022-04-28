# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    count += 1
                    queue = [(row, col)]
                    while queue:
                        curRow, curCol = queue.pop()
                        if 0 <= curRow < len(grid) and 0 <= curCol < len(grid[row]) and grid[curRow][curCol] == '1':
                            queue.extend(
                                [(curRow+1, curCol), (curRow-1, curCol), (curRow, curCol+1), (curRow, curCol-1)])
                            grid[curRow][curCol] = -1

        return count
