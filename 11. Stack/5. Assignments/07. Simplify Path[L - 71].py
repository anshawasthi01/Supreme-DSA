# https://leetcode.com/problems/simplify-path/description/

class Solution:
    # def buildAns(self, s, ans):
    #     if not s:
    #         return
    #     minPath = s.pop()
    #     self.buildAns(s, ans)
    #     ans += minPath

    def simplifyPath(self, path: str) -> str:
        s = []
        i = 0
        while i < len(path):
            start = i
            end = i + 1
            while end < len(path) and path[end] != '/':
                end += 1
            minPath = path[start:end]
            print(minPath)
            i = end  # Move to the next segment
            
            if minPath == '/' or minPath == '/.':
                pass
            elif minPath == '/..':
                if s:
                    s.pop()
            else:
                s.append(minPath)
            
        ans = ''.join(s) if s else '/'
        # self.buildAns(s, ans) # In cpp
        return ans



        # stack = []

        # # different directories present in the string
        # print(path)
        # temp = path.split('/') 
        # print(temp)

        # for i in temp:
        #     if i != '.' and i != '' and i != '..':
        #         stack.append(i) # add if it is directory

        #     # move to back directory if '..'
        #     elif i == '..':
        #         if stack:
        #             stack.pop()
        # # print(*stack)
        # return '/' + '/'.join(stack)