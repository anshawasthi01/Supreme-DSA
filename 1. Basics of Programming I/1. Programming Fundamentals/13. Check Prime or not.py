n = int(input())

if n > 1:
    for i in range(2, n//2):
        if (n % i) == 0:
            print("Not Prime")
            break
    else:
        print("Number is Prime")
else:
    print("This number is not a Prime Number")









