def solve(n, x, y, z):
    # base case
    if(n == 0):
        return 0

    if(n < 0):
        return -24370199

    ans1 = solve(n-x, x,y,z) + 1
    ans2 = solve(n-y, x,y,z) + 1
    ans3 = solve(n-z, x,y,z) + 1

    ans = max(ans1, max(ans2, ans3))
    return ans

n = 7
x = 5
y = 2
z = 2

# solve function -> returns maximum number of segments
ans = solve(n,x,y,z)
# ans -> valid && invalid

if(ans < 0):
    ans = 0
print("Answer is: ", ans)
