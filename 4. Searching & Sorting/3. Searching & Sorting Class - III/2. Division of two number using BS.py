# dividend = 10
# divisor = 2
# quotient = ?

def solve(dividend, divisor):
    s, e = 0, abs(dividend)
    ans = 0
    mid = s + (e - s)//2

    while s <= e:
        # perfect solution
        if abs(mid * divisor) == abs(dividend):
            ans = mid
            break
        # not perfect sol
        if abs(mid * divisor) > abs(dividend):
            # left
            e = mid - 1
        else:
            # ans store
            ans = mid
            # right search
            s = mid + 1
        mid = s + (e - s)//2

    if (divisor < 0) and (dividend < 0) or (divisor > 0) or (dividend > 0):
        return ans
    else:
        return -ans

dividend = -21
divisor = -7

ans = solve(dividend, divisor)
print("Ans is-> ", ans)
