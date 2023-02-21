# https://leetcode.com/problems/search-a-2d-matrix/
def binarySearch(arr, rows, cols, target):
    s, e = 0, rows*cols - 1
    mid = s + (e-s)//2

    while s <= e:
        rowIndex = mid//cols
        colIndex = mid%cols
    
        if arr[rowIndex][colIndex] == target:
            print("Found at ", rowIndex, " ", colIndex)
            return True
    
        if arr[rowIndex][colIndex] < target:
            s = mid +1

        else:
            e = mid - 1
        mid = s + (e-s)//2
    return False

arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]
rows, cols, target = 5, 4, int(input("Enter Target "))

ans = binarySearch(arr, rows, cols, target)

if ans:
    print("Found ") 
else:
    print("Not Found ") 





 
