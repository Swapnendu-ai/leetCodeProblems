# https://leetcode.com/problems/spiral-matrix/submissions/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowAdd = colAdd = 1
        row = col = 0
        incRow = False
        count = len(matrix)*len(matrix[0])
        elems = []
        while count > 0:
            elems.append(matrix[row][col])
            matrix[row][col] = None
            if incRow:
                if 0 <= row+rowAdd < len(matrix) and matrix[row+rowAdd][col] is not None:
                    row += rowAdd
                else:
                    incRow = False
                    rowAdd *= -1
                    col += colAdd
            else:
                if 0 <= col+colAdd < len(matrix[0]) and matrix[row][col+colAdd] is not None:
                    col += colAdd
                else:
                    incRow = True
                    colAdd *= -1
                    row += rowAdd
            count -= 1

        return elems
