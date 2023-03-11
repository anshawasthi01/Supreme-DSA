def palindrome(name):
    n = len(name)
    i, j = 0, n - 1

    while i<=j:
        if name[i] != name[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

st = ['N','O','O','N']
print(palindrome(st))



