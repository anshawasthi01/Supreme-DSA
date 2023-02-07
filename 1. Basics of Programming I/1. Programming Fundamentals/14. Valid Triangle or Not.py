# A Triangle if valid if sum of its two sides is greater than the third side

a, b, c = map(int, input().split())

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Not Valid")
else:
    print("Valid")


# Test : 7 10 5