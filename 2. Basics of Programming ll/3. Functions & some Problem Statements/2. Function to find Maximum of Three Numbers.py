a, b, c = map(int, input().split())

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
 
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
         
print(maximum(a, b, c))