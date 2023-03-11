def reverseCharArray(name):
    n = len(name)
    i, j = 0, n - 1

    while i<=j:
        name[i], name[j] = name[j], name[i]
        i += 1
        j -= 1      

st = ['A','N','S','H']
reverseCharArray(st)
print(st)