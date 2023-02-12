arr = list(map(int, input().split()))
key = int(input())

def LR(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True 
    return False

if LR(arr, key):
    print("Element", key, "is found in the array")
else:
    print("Element", key, "is not found in the array")
