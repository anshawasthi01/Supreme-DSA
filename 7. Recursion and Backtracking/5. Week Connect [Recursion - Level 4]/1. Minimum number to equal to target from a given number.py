def solve(arr, target):
    # base case
    if(target == 0):
        return 0

    if(target < 0):
        return 2437999

    # let's solve 1 case
    mini = 2437999
    for i in range(len(arr)):
        ans = solve(arr, target - arr[i]);
        if(ans != 2437999):
            mini = min(mini, ans + 1);
    return mini

arr = [1,2]
target = 5
ans = solve(arr, target)
print("Answer is: ", ans)