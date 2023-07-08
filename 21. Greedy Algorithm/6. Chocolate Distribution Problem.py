n = 7
m = 3
arr = [7, 3, 2, 4, 9, 12, 56]

# sort
arr.sort()

# check differences in m-size window
i = 0
j = m - 1
diff = float('inf')

while j < n:
    newDiff = arr[j] - arr[i]
    diff = min(diff, newDiff)
    j += 1
    i += 1

print("Answer is:", diff)
