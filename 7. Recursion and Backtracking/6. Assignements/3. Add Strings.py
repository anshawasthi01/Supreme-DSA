# https://leetcode.com/problems/add-strings/
# LeetCode : 415

class Solution:
    def addRE(self, num1, p1, num2, p2, carry, ans):
        # base case
        if p1 < 0 and p2 < 0:
            if carry != 0:
                ans.append(str(carry))
            return

        # ek case solve
        n1 = int(num1[p1]) if p1 >= 0 else 0
        n2 = int(num2[p2]) if p2 >= 0 else 0
        csum = n1 + n2 + carry
        digit = csum % 10
        carry = csum // 10
        ans.append(str(digit))

        # RE
        self.addRE(num1, p1 - 1, num2, p2 - 1, carry, ans)

    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        self.addRE(num1, len(num1) - 1, num2, len(num2) - 1, 0, ans)
        ans.reverse()
        return "".join(ans)




# class Solution {
# public:

# void addRE(string&num1, int p1, string&num2, int p2, int carry, string&ans){
#     // base case
#     if(p1 < 0 && p2 < 0){
#         if(carry != 0){
#             ans.push_back(carry + '0');
#         }
#         return;
#     }

#     // ek case solve
#     int n1 = (p1 >= 0 ? num1[p1] : '0') - '0';
#     int n2 = (p2 >= 0 ? num2[p2] : '0') - '0';
#     int csum = n1 + n2 + carry;
#     int digit = csum % 10;
#     carry = csum / 10;
#     ans.push_back(digit + '0');

#     // RE
#     addRE(num1, p1 - 1, num2, p2 - 1, carry, ans);

# }
#     string addStrings(string num1, string num2) {
#         string ans = "";
#         addRE(num1, num1.size()-1, num2, num2.size()-1, 0, ans);
#         reverse(ans.begin(), ans.end());
#         return ans;
        
#     }
# };




# GPT VERSION
# class Solution {
# void addRE(string num1, int p1, string num2, int p2, int carry, vector<char>& ans) {
#     // base case
#     if (p1 < 0 && p2 < 0) {
#         if (carry != 0) {
#             ans.push_back(carry + '0');
#         }
#         return;
#     }

#     // recursive case
#     int n1 = (p1 >= 0) ? (num1[p1] - '0') : 0;
#     int n2 = (p2 >= 0) ? (num2[p2] - '0') : 0;
#     int csum = n1 + n2 + carry;
#     int digit = csum % 10;
#     carry = csum / 10;
#     ans.push_back(digit + '0');

#     // recursive call
#     addRE(num1, p1 - 1, num2, p2 - 1, carry, ans);
# }

# public:
#     string addStrings(string num1, string num2) {
#                 vector<char> ans;
#         addRE(num1, num1.length() - 1, num2, num2.length() - 1, 0, ans);
#         reverse(ans.begin(), ans.end());
#         return string(ans.begin(), ans.end());
#     }
# };

