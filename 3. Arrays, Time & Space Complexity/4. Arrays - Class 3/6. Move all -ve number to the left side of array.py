# Dutch National Flag Alog Simply Two Pointer
def moveAllNegToLeft(a):
    l, h = 0, len(arr)-1
    while l<h:
        if a[l] < 0:
            l += 1
        elif a[h] > 0:
            h -= 1
        else:
            a[l], a[h] = a[h], a[l]


arr = [1, -3, 4, -5, 6]
moveAllNegToLeft(arr)

for i in range(len(arr)):
    print(arr[i])
