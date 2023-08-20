# https://practice.geeksforgeeks.org/problems/common-elements1132/1

# CodeHelp

class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        
        st = set()
        i, j, k = 0, 0, 0
        
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] and B[j] == C[k]:
                st.add(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        
        return sorted(list(st))



# class Solution
# {
#     public:    
#        vector <int> commonElements (int A[], int B[], int C[], int n1, int n2, int n3)
#         {
#             vector<int>res;
#             set<int>st;
#             int i,j,k;
#             i=j=k=0;
#             while(i<n1 && j<n2 && k<n3){
#                 if (A[i] == B[j] && B[j] == C[k]){
#                     st.insert(A[i]);
#                     i++,j++,k++;
#                 }
#                 else if(A[i]<B[j]){
#                     i++;
#                 }
#                 else if(B[j]<C[k]){
#                     j++;
#                 }
#                 else{
#                     k++;
#                 }
#             }
#             for(auto i:st){
#                 res.push_back(i); 
#             }
#         return res;
#         }
# };