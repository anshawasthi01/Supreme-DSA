def printSubsequences(strr, n, output, i, v):
    # base case
    if(i == n ):
        v.append(output)
        return

    # include
    printSubsequences(strr, n, output + strr[i], i+1, v);

    # exclude
    printSubsequences(strr, n, output, i+1, v)

strr = "abcd"
output = ""
v = []
i = 0
n = len(strr)
printSubsequences(strr, n, output, i, v)

print("Printing all subsequences " )
for val in v:
    print(val, " ", end = ' ')

print()
print("Size of vector is: ", len(v))



