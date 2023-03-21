# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
# Leetcode 1910

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        
        start_ind = s.index(part)
        
        removed_string = s[:start_ind] + s[(start_ind+len(part)):]
        
        return self.removeOccurrences(removed_string, part)







# # Iterative
#         while(part in s):
#             s=s.replace(part,"",1)
#         return s
