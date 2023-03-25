# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


# CodeHelp

class Solution:
    def solve(self, ans, index, output, digits, mapping):
        # base case
        if index >= len(digits):
            ans.append(output)
            return
        
        # 1 case solve, baaki recursion
        digitCharacter = digits[index]
        digitInteger = int(digitCharacter)
        value = mapping[digitInteger]
        
        for ch in value:
            # include
            # output += ch
            # recursive call
            self.solve(ans, index+1, output + ch, digits, mapping)
            # backtrack
            # output = output[:-1]
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # empty string k liye answer empty array hoga
        if not digits:
            return ans
        
        index = 0
        output = ""
        mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # mapping = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        # mapping = {}
        # mapping[2] = "abc"
        # mapping[3] = "def"
        # mapping[4] = "ghi"
        # mapping[5] = "jkl"
        # mapping[6] = "mno"
        # mapping[7] = "pqrs"
        # mapping[8] = "tuv"
        # mapping[9] = "wxyz"
        
        self.solve(ans, index, output, digits, mapping)
        return ans