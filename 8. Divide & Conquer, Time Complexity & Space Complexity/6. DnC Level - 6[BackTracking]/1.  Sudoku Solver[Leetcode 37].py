# https://leetcode.com/problems/sudoku-solver/

# CodeHelp

def isSafe(row, col, board, value):
    n = len(board)

    for i in range(n):
        # row check
        if board[row][i] == value:
            return False

        # col check
        if board[i][col] == value:
            return False

        # 3x3 box check
        # if board[      3*(row/3)          +   (i/3)    ][3*(col/3)+(i%3)] == value:
        #         starting row of a boxes      movement

        if board[3*(row//3) + (i//3)][3*(col//3) + (i%3)] == value:
            return False

    return True

def solve(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            # check for empty cell
            if board[i][j] == '.':
                # try to fill with values ranging from 1 to 9
                for val in range(1, 10):
                    val = str(val)
                    # check for safety
                    if isSafe(i, j, board, val):
                        # insert
                        board[i][j] = val
                        # recursion sambal lega
                        remainingBoardSolution = solve(board)
                        if remainingBoardSolution:
                            return True
                        else:
                            # backtrack
                            board[i][j] = '.'

                # if 1 se 9 tak koi bhi value se solution
                # nahi nikla ,current cell pr
                # that means there is a mistake somewhere,
                # go back by returning false
                return False

    # all cells filled
    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        solve(board)