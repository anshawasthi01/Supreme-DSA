def solve(arr, i, summ, maxi):
    # base case
    if(i >= len(arr)):
        # maxi update
        maxi[0] = max(summ, maxi[0])
        return 

    # include
    solve(arr, i+2, summ+arr[i], maxi)
    # exclude
    solve(arr, i+1, summ, maxi)

arr = [1, 2, 3, 1, 3, 5, 8, 1, 9]
summ = 0
maxi = [-2437999]
i = 0
solve(arr, i, summ, maxi)
print(maxi[0])

