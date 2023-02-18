# https://www.geeksforgeeks.org/factorial-large-number/
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def factorial(self, N):
        ans = []
        ans.append(1)
        carry = 0
        for i in range(2, N+1):
            for j in range(len(ans)):
                x = ans[j] * i + carry
                ans[j] = x % 10
                carry = x//10
                
            while(carry):
                ans.append(carry%10)
                carry //= 10
        
        return ans[::-1]


# class Solution {
# public:
#     vector<int> factorial(int n){
#         // code here
#         vector<int>res;
#         res.push_back(1);
        
#         for(int i =2;i<=n;i++){
#             int carry =0;
#             for(int j =0; j<res.size();j++){
#                 int val = res[j]*i+carry;
#                 res[j] = val%10;
#                 carry = val/10;
#             }
            
#             while(carry){
#                 res.push_back(carry%10);
#                 carry/=10;
#             }
#         }
#         reverse(res.begin(),res.end());
#         return res;   
#     }
# };