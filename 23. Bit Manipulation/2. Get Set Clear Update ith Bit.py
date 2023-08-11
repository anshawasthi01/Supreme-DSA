def getithBit(n, i):
    mask = 1 << i
    ans = n & mask
    if ans == 0:
        return 0
    else:
        return 1

def setithBit(n, i):
    mask = 1 << i
    ans = n | mask
    print("After setting:", ans)

def clearIthBit(n, i):
    mask = ~(1 << i)
    n = n & mask
    # print("After clearing:", n)
    return n

# GENERIC
def updateIthBit(n, i, target):
    n = clearIthBit(n, i)
    mask = target << i
    n = n | mask
    print("after updating:", n)

# Testing the functions
ans = getithBit(10, 0)
print(ans)

setithBit(10, 2)

n = 10
n = clearIthBit(n, 0)
print("After clearing:", n)

n = 10
# 0 bit ko 1 set krdo
# GENERIC
updateIthBit(n, 0, 1)