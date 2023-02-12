arr = [0,1,1,1,0,0,0,0,1,0,1,0,1,0,1, 2, 4 ,5, 7]
size = 19
numTwo = 0

for i in range(size):
    if arr[i] == 2:          # if 2 found, increment numTwo
        numTwo += 1

print("number of Two's ", numTwo )
