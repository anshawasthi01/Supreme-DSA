# https://github.com/anshawasthi01/Supreme-DSA/blob/main/4.%20Searching%20%26%20Sorting/2.%20Searching%20%26%20Sorting%20Class%20-%20II/BS%202%20Cods/main%20(2).cpp
# https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/

# BS 2 Cods main(3).cpp
def findSqrt(n):
    target = n 
    s = 0
    e = n 
    ans = -1
    while s <= e:
        mid = s + (e-s)//2
        if mid*mid == target:
            return mid  

        if mid*mid > target:
            e = mid - 1         # left search

        else:
            ans = mid           # ans store
            s = mid+1           # right search
    return ans

n = int(input("Enter the number "))
ans = findSqrt(n)
print("Ans is ", ans)

precision = int(input("Enter the number of floating digits in precison "))
step = 0.1
finalAns = ans
for i in range(precision):
    j = finalAns
    while j*j<=n:
        finalAns = j
        j+=step
    step = step / 10
print("Final ans is. ", round(finalAns, precision))


# precision = int(input("Enter the number of floating digits in precison "))
# step = 0.1
# for i in range(precision):
#     while ans*ans<=n:
#         ans += step
#     ans = ans - step
#     step = step / 10
# print("Final ans is. ", round(ans, precision))

#      for(double j=finalAns; j*j<=n; j = j + step) {
#         finalAns = j;
#      }
#   /  step = step / 10;