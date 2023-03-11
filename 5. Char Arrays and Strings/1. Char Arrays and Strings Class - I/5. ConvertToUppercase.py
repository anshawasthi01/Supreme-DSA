print("Enter the Character: ", end="")
ch = input()

chlen = len(ch)
if chlen==1:
    if ch>='a' and ch<='z':
        chup = ord(ch)
        chup = chup-32
        chup = chr(chup)
        print("\nIts Uppercase is: ", chup)
    elif ch>='A' and ch<='Z':
        print("\nAlready in Uppercase!")
    else:
        print("\nInvalid Input!")
else:
    print("\nInvalid Input!")