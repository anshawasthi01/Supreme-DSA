# Gives common Element
# Linear Search

arr = [1,2,3,3,4,6,8]
brr = [3,3,4,10]
ans = []

# outer loop on arr vector
for i in range(len(arr)):
    element = arr[i]
    # for every element, run loop on brr
    for j in range(len(brr)):
        if element == brr[j]:
            # mark
            brr[j] = -1
            ans.append(element)
		
# print ans 
for i in range(len(ans)):
    print(ans[i], " ")