# https://practice.geeksforgeeks.org/problems/count-the-reversals0401/1

# CodeHelp Stack

def countRev (s):
    # if odd sized string then impossible to make pairs
    if len(s) & 1: return -1
    
    ans = 0
    st = []
    for c in s:
        if c == '{':
            st.append(c)
        else:
            if st and st[-1] == '{':
                st.pop()
            else:
                st.append(c)
                
    # if stack is still not empty, let's count reversals
    while st:
        a = st.pop()
        b = st.pop()
        if a == b:
            ans += 1
        else:
            ans += 2

    return ans  