def checkPowerOf2(n):
    if (n & (n - 1)) == 0:
        return True
    else:
        return False

print("Power of 2 ans:", checkPowerOf2(4))