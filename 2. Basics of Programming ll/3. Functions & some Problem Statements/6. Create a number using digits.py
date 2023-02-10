arr = list(map(int, input().split()))
# 8 2 3 7
ans = 0
for i in range(len(arr)):
    ans = ans * 10 + arr[i]

print(ans)