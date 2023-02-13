# Pair Sum
arr = [10,20,40,60,70]
sum = 80

# print all pairs
# outer loop will traverse for each element
for i in range(len(arr)):
    element = arr[i]
    # for every element, will traverse on aage wale elements
    for j in range(i+1, len(arr)):
        if element + arr[j] == sum:
            print("Pair Found", element, " ", arr[j])
