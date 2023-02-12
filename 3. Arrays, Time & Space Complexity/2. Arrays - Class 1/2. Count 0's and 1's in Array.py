arr = [0,1,1,1,0,0,0,0,1,0,1,0,1,0,1, 2, 4 ,5, 7]
size = 19
numZero = 0
numOne = 0

for i in range(size):
    if arr[i] ==0:          # if zero found, increment numZero
        numZero += 1
        
    if arr[i] == 1:          # if One found, increment numOne
        numOne += 1

print("number of zeroes ", numZero )
print("number of ones ", numOne )