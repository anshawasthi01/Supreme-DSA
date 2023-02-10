# sets bit means how many count of 1 bit

n = int(input())

ans = 0
while n > 0:
    # found one set bit, so increment set bit count
    ans += n & 1
    # if n & 1:
    #     ans += 1
    n = n >> 1

print(ans)