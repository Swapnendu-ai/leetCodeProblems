# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(l):
            lSet = set(l)
            return len(lSet) == len(l)

        columns = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for rowNum, row in enumerate(board):
            rowData = []
            for col, val in enumerate(row):
                if val != '.':
                    columns[col].append(val)
                    squareRow = rowNum//3
                    squareCol = col // 3
                    squares[squareRow*3+squareCol].append(val)
                    rowData.append(val)

            if not validate(rowData):
                return False

        for col in columns:
            if not validate(col):
                return False

        for square in squares:
            if not validate(square):
                return False

        return True
