import sys
arr = [2,4,6,1,3,7,9,12,56,43,21]
size = 11
# initialse the maxi variable with the 
# minimum possible integer value
maxi = sys.maxsize
mini =sys.maxsize

for i in range(size):
    if arr[i] < mini:
        # found a number gretaer than maxi, update maxi
        mini = arr[i]

print("minimum number is ",mini )