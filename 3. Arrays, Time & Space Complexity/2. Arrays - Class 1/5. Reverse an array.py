arr = [10,20,30,40,50,60,70]
size = 7

start = 0
end = size-1

def standard(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]       # step1
        start += 1                                          # step2
        end -= 1                                            # step13                       

    for i in range(size):     # printing array
        print(arr[i], " ", end = ' ')


def temp(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
      
        start += 1                                         
        end -= 1                                                                

    for i in range(size):     # printing array
        print(arr[i], " ", end = ' ')


def xor(arr, start, end):
    while start <= end:
        arr[start]^=arr[end]
        arr[end]^=arr[start]
        arr[start]^=arr[end]
    
        start += 1                                         
        end -= 1                                                                

    for i in range(size):     # printing array
        print(arr[i], " ", end = ' ')


def PlusMinus(arr, start, end):
    while start <= end:
        arr[start]=arr[start]+arr[end]
        arr[end]=arr[start]-arr[end]
        arr[start]=arr[start]-arr[end]
      
        start += 1                                         
        end -= 1                                                                

    for i in range(size):     # printing array
        print(arr[i], " ", end = ' ')

standard(arr, start, end)
temp(arr, start, end)
xor(arr, start, end)
PlusMinus(arr, start, end)

# x = x*y
# t = x/y
# x = x/y



