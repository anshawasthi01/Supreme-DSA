mat = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
      ]

def WavePrint(mat):
    m = len(mat)
    n = len(mat[0])

    for startCol in range(n):
        # even no of col-> Top to bottom
        if startCol & 1 == 0:
            for i in range(m):
                print(mat[i][startCol]," ",end='')

        else:
            for i in range(m-1, -1, -1):
                print(mat[i][startCol]," ", end='')

WavePrint(mat)
