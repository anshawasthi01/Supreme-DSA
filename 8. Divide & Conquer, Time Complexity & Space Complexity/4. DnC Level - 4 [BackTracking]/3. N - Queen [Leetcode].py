# Leetcode - 51 https://leetcode.com/problems/n-queens/description/

class Solution:
    def storeSolution(self, board, n, ans):
        temp = []
        for i in range(n):
            output = ""
            for j in range(n):
                output += board[i][j]
            temp.append(output)
        ans.append(temp)

    def isSafe(self, row, col, board, n):
        if rowCheck[row] == True:
            return False
        if upperLeftDiagonalCheck[n-1+col-row]:
            return False
        if bottomLeftDiagonalCheck[row+col]:
            return False
        return True

    def solve(self, board, col, n, ans):

        # base case
        if col >= n:
            self.storeSolution(board, n, ans)
            return

        # 1 case solve karna h , baaki recursion sambhal lega
        # try to place a queen in each row of the current column
        for row in range(n):
            
            if self.isSafe(row, col, board, n):
                # rkh do
                # place a queen at (row, col)
                board[row][col] = 'Q'
                rowCheck[row] = True
                upperLeftDiagonalCheck[n-1+col-row] = True
                bottomLeftDiagonalCheck[row+col] = True

                # recursion soluion lgega
                # try to place queens in the next columns
                self.solve(board, col+1, n, ans)

                # backtracking
                # backtrack and remove the queen from (row, col)
                board[row][col] = '.'
                rowCheck[row] = False
                upperLeftDiagonalCheck[n-1+col-row] = False
                bottomLeftDiagonalCheck[row+col] = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        global rowCheck
        global upperLeftDiagonalCheck
        global bottomLeftDiagonalCheck

        rowCheck = {i: False for i in range(n)}
        upperLeftDiagonalCheck = {i: False for i in range(2*n-1)}
        bottomLeftDiagonalCheck = {i: False for i in range(2*n-1)}
        board = [['.' for j in range(n)] for i in range(n)]
        ans = []
        col = 0
        # 0 -> empty cell
        # 1 -> Queen at the cell
        
        self.solve(board, col, n, ans)
        return ans






