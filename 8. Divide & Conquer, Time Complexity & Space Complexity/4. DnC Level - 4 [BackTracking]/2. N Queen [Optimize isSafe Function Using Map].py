def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print("\n")

def isSafe(row, col, board, n):
    if rowCheck[row]:
        return False
    if upperLeftDiagonalCheck[n-1+col-row]:
        return False
    if bottomLeftDiagonalCheck[row+col]:
        return False
    return True

    # # check karna chahte h , k kya main 
    # # current cell [row,col] pr    QUEEN rakh 
    # # sakta hu ya nahi
    # # check if it is safe to place a queen at current cell (row, col)
    # i, j = row, col

    # # check row
    # while j >= 0:
    #     if board[i][j] == 'Q':
    #         return False
    #     j -= 1

    # # check upper left diagonal
    # i, j = row, col
    # while i >= 0 and j >= 0:
    #     if board[i][j] == 'Q':
    #         return False
    #     i -= 1
    #     j -= 1

    # # check bottom left diagonal
    # i, j = row, col
    # while i < n and j >= 0:
    #     if board[i][j] == 'Q':
    #         return False
    #     i += 1
    #     j -= 1

    # # kahin pr bhi queen nahi mili
    # # iska matlab ye position safe hai 
    # # iska matlab eturn kardo true
    # # if no queen found in the same row or the two diagonals,
    # # it is safe to place a queen at current cell
    # return True

def solve(board, col, n):
    # base case
    if col >= n:
        printSolution(board, n)
        return

    # 1 case solve karna h , baaki recursion sambhal lega
    # try to place a queen in each row of the current column
    for row in range(n):
        if isSafe(row, col, board, n):
            # rkh do
            # place a queen at (row, col)
            board[row][col] = 'Q'
            rowCheck[row] = True
            upperLeftDiagonalCheck[n-1+col-row] = True
            bottomLeftDiagonalCheck[row+col] = True

            # recursion soluion lgega
            # try to place queens in the next columns
            solve(board, col+1, n)

            # backtracking
            # backtrack and remove the queen from (row, col)
            board[row][col] = '.'
            rowCheck[row] = False
            upperLeftDiagonalCheck[n-1+col-row] = False
            bottomLeftDiagonalCheck[row+col] = False

n = 4
board = [['-' for j in range(n)] for i in range(n)]
col = 0
# 0 -> empty cell
# 1 -> Queen at the cell

rowCheck = {i: False for i in range(n)}
upperLeftDiagonalCheck = {i: False for i in range(2*n-1)}
bottomLeftDiagonalCheck = {i: False for i in range(2*n-1)}

solve(board, col, n)