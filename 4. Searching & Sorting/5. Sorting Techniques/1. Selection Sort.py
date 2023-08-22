# starting se traverse krenge jo b minimum number milega usko i = 0 pr rkh denge or i+=1 kar denge

arr = [5,4,3,2,1]
n = len(arr)
# selection sort
# outer loop -> (n-1) rounds
for i in range(n-1):
    minIndex = i
    # inner Loop -> index of minimum element in range i->n
    for j in range(i+1, n):
        if arr[j] < arr[minIndex]:
            # new minimum, then store
            minIndex = j

        # swap
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

# printing 
for i in range(n):
    print(arr[i], end=" ")


