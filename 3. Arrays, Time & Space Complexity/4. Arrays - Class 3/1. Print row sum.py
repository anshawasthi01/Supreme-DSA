R, C = map(int, input().split())
  
matrix = []

for i in range(R):        
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix.append(a)
  

for i in range(R):
    sm = 0
    for j in range(C):
        sm = sm + matrix[i][j]
    print(sm, end='  ')