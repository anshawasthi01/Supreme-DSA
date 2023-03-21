def binarySearch(arr, s, e, key):
    # base case

    if(s > e):
        return -1
  
    mid = (s+e)//2
    if(arr[mid] == key):
        return mid

    if(arr[mid] < key):
        s = mid+1
        ans =  binarySearch(arr,s,e, key)
        return ans
  
    else:
        e= mid-1
        ans =  binarySearch(arr,s,e, key)
        return ans

v = [10,20,40,60,70,90,99]
target = 99

n = len(v)
s = 0
e = n-1
ans = binarySearch(v, s, e, target )

print("Answer is: ", ans)
