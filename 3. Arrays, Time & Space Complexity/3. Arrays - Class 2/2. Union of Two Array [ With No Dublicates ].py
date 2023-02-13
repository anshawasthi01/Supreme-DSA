arr = [1,3,5,7,9]
brr = [2,4,6,8]

ans = []

# push all element of vector arr
for i in range(len(arr)):
    ans.append(arr[i])


# push all element of vector brr
for i in range(len(brr)):
    ans.append(brr[i])

# print ans
print("Printing ans array ")
for i in range(len(ans)):
    print(ans[i], " ", end='')

