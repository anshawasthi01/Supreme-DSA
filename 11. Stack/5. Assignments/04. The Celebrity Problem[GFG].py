# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# CodeHelp Stack

class Solution:
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        st = []
        
        # step 1: append all persons into stack
        for i in range(n):
            st.append(i)
            
        # step 2: run discarded method, to get a mightBeCelebrity
        while len(st) != 1:
            a = st.pop()
            b = st.pop()
            
            # if a knows b
            if M[a][b]:
                # a is not celebrity, b might be
                st.append(b)
            
            else:
                # b is not celebrity, a might be
                st.append(a)
                
        # step 3: Check that single person is actually celebrity?
        mightBeCelebrity = st.pop()
        
        # Celebrity should not know anyone
        for i in range(n):
            if M[mightBeCelebrity][i] != 0:
                return -1
                
        # everyone should know celebrity
        for i in range(n):
            if M[i][mightBeCelebrity] == 0 and i != mightBeCelebrity:
                return -1
            
        # mightBeCelebrity is celebrity
        return mightBeCelebrity