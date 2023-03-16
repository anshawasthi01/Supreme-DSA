# https://leetcode.com/problems/longest-common-prefix/description/

# CodeHelp
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # strs = ["flower","flow","flight"]
        ans = ""
        i = 0
        while(True):
            curr_ch = 0
            for strr in strs:
                if i >= len(strr):
                    # out of Bound
                    curr_ch = 0
                    break
                
                # just started
                if curr_ch == 0:
                    curr_ch = strr[i]

                elif strr[i] != curr_ch:
                    curr_ch = 0
                    break

            if curr_ch == 0:
                break
            
            ans += curr_ch
            i += 1

        return ans























        # short = min(strs, key=len) # short = "flow"
        # for item in strs: # When item = "flight"
        #     while len(short) > 0:
        #         if item.startswith(short): # during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
        #             break
        #         else:
        #             short = short[:-1] # during loop 1 short = flo, during loop 2 short = fl
        # return short