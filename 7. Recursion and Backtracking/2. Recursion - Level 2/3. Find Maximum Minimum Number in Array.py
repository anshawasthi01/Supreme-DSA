def findMax(arr, n, i, maxi):
        # base case
        if(i >= n):
            print(maxi)
            # array agar khtam hogya, poora traverse hogya
            # toh wapas aajao
            return

        # 1 case solve krna h 
        # current element ko cjheck karo for max
        if(arr[i] > maxi):
            maxi = arr[i]
        
        # baaki recursion sambhal lega
        findMax(arr, n, i+1, maxi);

def findMin(arr, n, i, mini):
        # base case
        if( i >= n):
            print(mini)
            return
        
        # 1 case solve krna padega
        mini = min(mini, arr[i])

        # baaki recursion sambhal lega
        findMin(arr, n, i+1, mini)

arr = [10,30,21,44,32,6,19,66]
n = 8
maxi = -9999999
mini = 9999999

i = 0
findMax(arr, n, i, maxi)
findMin(arr, n, i, mini)
# print("maximum number is: ", maxi)
# print("minimum number is: ", mini)
# Interger Variable always pass by value in python
