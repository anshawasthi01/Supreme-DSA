def lastOccLTR(s, x, i, ans):
    # base case
    if i >= len(s):
        return

    # ek case solution
    if s[i] == x:
        ans[0] = i 

    # RE
    lastOccLTR(s, x, i+1, ans)


def lastOccRTL(s, x, i, ans):
    # base case
    if i < 0:
        return

    # ek case solution
    if s[i] == x:
        ans[0] = i 
        return

    # RE
    lastOccRTL(s, x, i-1, ans)

s = "Ansh Awasthi"
x = 'a'

ans = [-1]
# lastOccLTR(s, x, 0, ans)
lastOccRTL(s, x, len(s)-1, ans)
print(ans[0])
