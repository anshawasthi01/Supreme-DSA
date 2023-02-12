arr = [10,20,30,40,50,60,70,80]
size = 8

start = 0
end = size-1

while start <= end:
    
    if start == end:
        print(arr[start]," ")
    else:
        print(arr[start], " ")
        print(arr[end], " ")
        
    start += 1
    end -= 1

