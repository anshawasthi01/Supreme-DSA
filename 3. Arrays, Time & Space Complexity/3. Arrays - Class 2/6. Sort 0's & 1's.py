arr = [0,1,0,1,1,0,1,0,1,1]
start = 0;
end = len(arr)-1
i = 0

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i]," ", end='')


while i != end:
    print("for i=", i, " start=", start, " end=", end)
    if(arr[i] == 0):
        print("found zero")
        print("before swap ")
        printArray(arr)
        
        arr[start], arr[i] = arr[i], arr[start]
        print("after  swap ")
        printArray(arr)
        start += 1
        i += 1
        print("now i=", i,  " start=", start, " end=", end )
    else:
        arr[end], arr[i] = arr[i], arr[end]
        end -= 1
        print("now i=", i,  " start=", start, " end=", end )

# print
for i in range(len(arr)):
    print(arr[i], end='  ')

	