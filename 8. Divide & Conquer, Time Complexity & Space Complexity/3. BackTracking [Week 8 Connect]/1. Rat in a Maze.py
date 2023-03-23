def isSafe(i, j, row, col, arr, visited):
    if i >= 0 and i < row and j >= 0 and j < col and arr[i][j] == 1 and not visited[i][j]:
        return True
    return False

def solveMaze(arr, row, col, i, j, visited, path, output):
  # base case
    if i == row - 1 and j == col - 1:
      # answer found
        path.append(output)
        return
    
    # down -> (i+1,j)
    if isSafe(i + 1, j, row, col, arr, visited):
        visited[i + 1][j] = True
        solveMaze(arr, row, col, i + 1, j, visited, path, output + 'D')
        # backtrack
        visited[i + 1][j] = False
        
    # left -> (i,j-1)
    if isSafe(i, j - 1, row, col, arr, visited):
        visited[i][j - 1] = True
        solveMaze(arr, row, col, i, j - 1, visited, path, output + 'L')
        # backtrack
        visited[i][j - 1] = False
        
    # right -> (i,j+1)
    if isSafe(i, j + 1, row, col, arr, visited):
        visited[i][j + 1] = True
        solveMaze(arr, row, col, i, j + 1, visited, path, output + 'R')
        # backtrack
        visited[i][j + 1] = False
        
    # up -> (i-1,j)
    if isSafe(i - 1, j, row, col, arr, visited):
        visited[i - 1][j] = True
        solveMaze(arr, row, col, i - 1, j, visited, path, output + 'U')
        # backtrack
        visited[i - 1][j] = False

arr = [ 
        [1, 0, 0, 0], 
        [1, 1, 0, 1], 
        [1, 1, 0, 0], 
        [0, 1, 1, 1]
      ]

if arr[0][0] == 0:
    print("No Path Exists")

else:
  row = 4
  col = 4

  visited = [[False for j in range(col)] for i in range(row)]
  # src ki value ko true kar dete hain
  visited[0][0] = True

  path = []
  output = ""

  solveMaze(arr, row, col, 0, 0, visited, path, output)

  print("printing the results")
  for i in path:
      print(i, end=" ")
  print()

  if len(path) == 0:
      print("No Path Exists")