def print1(arr, n, i):
        # base case
        if( i >= n):
                return

        # 1 case solve krdia
        print(arr[i], "->", end = ' ')
        # baaki recursion sambhal lega
        print1(arr, n, i+1)

def print2(arr, n):
        # base case
        if( n==0):
            return

        # 1 case solve krdia
        print(arr[0], " ")
        #  baaki recursion sambhal lega
        print2(arr+1, n-1)

arr = [10,20,30,40,50]
n = 5
i = 0
print1(arr, n,i)

