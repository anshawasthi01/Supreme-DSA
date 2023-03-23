# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

def isSafe(i, j, row, col, arr, visited):
  if i >= 0 and i < row and j >= 0 and j < col and arr[i][j] == 1 and not visited[i][j]:
    return True
  else:
    return False
    
def solveMaze(arr, row, col, i, j, visited, path, output):
  # base case
  if i == row-1 and j == col-1:
    # answer found
    path.append(output)
    return

  # down -> (i+1,j)
  if isSafe(i+1, j, row, col, arr, visited):
    visited[i+1][j] = True
    solveMaze(arr, row, col, i+1, j, visited, path, output+'D')
    # backtrack
    visited[i+1][j] = False

  # left -> (i,j-1)
  if isSafe(i, j-1, row, col, arr, visited):
    visited[i][j-1] = True
    solveMaze(arr, row, col, i, j-1, visited, path, output+'L')
    # backtrack
    visited[i][j-1] = False

  # right -> (i,j+1)
  if isSafe(i, j+1, row, col, arr, visited):
    visited[i][j+1] = True
    solveMaze(arr, row, col, i, j+1, visited, path, output+'R')
    # backtrack
    visited[i][j+1] = False

  # up -> (i-1,j)
  if isSafe(i-1, j, row, col, arr, visited):
    visited[i-1][j] = True
    solveMaze(arr, row, col, i-1, j, visited, path, output+'U')
    # backtrack
    visited[i-1][j] = False


class Solution:
    def findPath(self, arr, n):

        row = n
        col = n
        path = []
        output = ""
        visited = [[False for j in range(col)] for i in range(row)]
        if arr[0][0] == 0:
            return path
        # src ki value ko true mark krenge rat jaha se start krega

        visited[0][0] = True
        solveMaze(arr, row, col, 0, 0, visited, path, output)
        return path