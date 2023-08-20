
# https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-two-arrays2408/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# https://www.geeksforgeeks.org/add-two-numbers-represented-by-two-arrays/

def helperAdd(a, b, n, m) :
    carry = 0
    ans = ''
    i = n-1
    j = m-1
        
    while i >= 0 and j >= 0:
        x = a[i] + b[j] + carry
        ans += str(x % 10)
        carry = x // 10  # In cpp /
        i -= 1
        j -= 1
            
    while i >= 0:
        x = a[i] + carry
        ans += str(x % 10)
        carry = x // 10     # In cpp /
        i -= 1
            
    while j >= 0:
        x = b[j] + carry
        ans += str(x % 10)
        carry = x // 10    # In cpp /
        j -= 1
    
    if carry == 1:
        ans += str(carry)
    return int(ans[::-1])

class Solution:
    # def calc_Sum (self, a,  n, b, m) :
        # f = ""
        # s = ""  # a.push_back(digit+ '0')
        # for i in arr:
        #     f += str(i)
        # for i in brr:
        #     s += str(i)
        # return int(f) + int(s)
        
    def calc_Sum (self, a1,  n1, a2, n2) :
        if n1 < n2:
            return helperAdd(a2,a1,n2,n1)
        return helperAdd(a1,a2,n1,n2)