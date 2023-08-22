# saare number 2-2 ke pair m honge 2 se jyada kisi bhi number ka pair ek sath nahi hoga
# odd element 1 baar hi aayega 
# odd number ko chodkr baaki saare number pair mein honge

def solve(arr):
    s = 0
    e = len(arr) - 1
    mid = s + (e-s)//2

    while(s <= e):
        if(s == e):
        # single element
            return s


        # 2 cases -> mid - even or mid - odd
        if(mid%2 == 0 ):
            if(arr[mid] == arr[mid + 1] ):
                s = mid + 2
    
            else:
                e = mid

        else:
            if(arr[mid] == arr[mid-1]):
                s = mid + 1

            else:
                e = mid - 1
        mid = s + (e-s)//2
    return -1



arr = [1,1,2,2,3,3,1,4,4,2,2,4,4]
ans = solve(arr)
print("index is ", ans)
print("value is ", arr[ans])

