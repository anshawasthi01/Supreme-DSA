def solve(arr, n, k):
    q = []
    # Process first window of size k
    for i in range(k):
        if arr[i] < 0:
            q.append(i)

    # Remaining window ko process kro
    for i in range(k, n):
        # Answer dedo purani wondow ka
        if not q:
            print(0, end=' ')
        else:
            print(arr[q[0]], end=' ')

        # Out of window elements ko remove krdo
        while q and i - q[0] >= k:
            q.pop(0)

        # Check current element for insertion
        if arr[i] < 0:
            q.append(i)

    # Answer print karonfor last window
    if not q:
        print(0, end=' ')
    else:
        print(arr[q[0]], end=' ')
        

# Driver code
arr = [12,-1,-7,8,-15,30,16,28]
n = len(arr)
k = 3
solve(arr, n, k)
