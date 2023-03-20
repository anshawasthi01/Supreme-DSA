def printDigits(n):
        # base case
        # print("Prining value of n ", n)
        if(n == 0 ):
                return

        # baaaki recursion sambhal lega
        printDigits( n // 10)

        # 1 case main solve karunga
        digit = n % 10
        print(digit, " ", end = ' ')

# HW
n = 647  # 0006545 : starting with 0 cause error
print(n)
if(n == 0):
    print(0)
        
printDigits(n)

# ans = [10] * 20
# for i in range(len(ans)):
#     print(ans[i])
