arr = [ [12, 2, 3],
        [1, 3, 7],
        [4, 6, 8]
      ]
r = len(arr)
c = (len(arr[0]))


transposeArr = [ [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]
               ]

def transpose(arr, r, c, transposeArr):
    for i in range(r):
        for j in range(c):
            transposeArr[j][i] = arr[i][j]

def printArray(arr, r, c):
    for i in range(r):
        for j in range(c):
            print(transposeArr[i][j], " ", end = ' ')
        print()

transpose(arr, r, c, transposeArr)
printArray(arr, r, c)