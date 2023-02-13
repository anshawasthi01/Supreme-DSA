import sys
arr = [ [12, 2, 3],
        [1, 3, 7],
        [4, 6, 8]
      ]


def getMaxi(arr, rows, cols):
    maxi = -2147783647
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] > maxi:
                maxi = arr[i][j]

    return maxi

rows = len(arr)
cols = (len(arr[0]))
print(getMaxi(arr, rows, cols))
