def ifPalindrome(s, start, end):
    # base case
    if start >= end:
        return True 
    
    # one case solution
    if s[start] != s[end]:
        return False 

    return ifPalindrome(s, start + 1, end - 1)

s = "AMA"
print(ifPalindrome(s, 0, len(s) - 1))