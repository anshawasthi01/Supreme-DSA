def printMiddle(s, totalSize):
    if len(s) == 0:
        print("There is no element in stack")
        return
    
    # base case
    if len(s) == totalSize//2 + 1:
        print("Middle element is:", s[-1])
        return
    temp = s.pop()
    # recursive call
    printMiddle(s, totalSize)
    # backtrack
    s.append(temp)

s = []
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
s.append(60)
s.append(70)

totalSize = len(s)
printMiddle(s, totalSize)
