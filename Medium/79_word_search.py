# https://leetcode.com/problems/word-search/

from typing import List


class Solution:

    def inRange(self,i,j):
        return 0 <=i < len(self.board) and 0<= j < len(self.board[0])

    def search(self,word,i,j):
        if len(word) == 0:
            return True
        self.visited[i][j] = True

        for rowNeighbor in [i-1,i+1]:
            if (self.inRange(rowNeighbor,j)
                        and not self.visited[rowNeighbor][j]
                        and word[0] == self.board[rowNeighbor][j]):
                    if self.search(word[1:],rowNeighbor,j):
                        return True
        for colNeighbor in [j-1,j+1]:
            if (self.inRange(i,colNeighbor)
                    and not self.visited[i][colNeighbor]
                    and word[0] == self.board[i][colNeighbor]):
                if self.search(word[1:],i,colNeighbor):
                    return True

        self.visited[i][j] = False
        return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.visited = [[False for _ in rowI] for rowI in board]
        for i,row in enumerate(board):
            for j,char in enumerate(row):
                if char == word[0]:
                    if self.search(word[1:],i,j):
                        return True

        return False

print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))
print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
