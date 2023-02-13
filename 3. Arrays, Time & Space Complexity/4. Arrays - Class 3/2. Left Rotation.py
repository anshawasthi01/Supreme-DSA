arr = [ [1, 2, 3],
        [1, 3, 7],
        [4, 6, 8]
      ]
key = 5

def findKey(arr, rows, cols, key):
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == key:
                return True 
    return False

rows = len(arr)
cols = len(arr[0])
print(findKey(arr, rows, cols, key))



