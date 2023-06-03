 # CodeHelp

class TrieNode:
    def __init__(self, d):
        self.data = d
        self.children = [None] * 26
        self.isTerminal = False
        self.childCount = 0

def insertWord(root, word):
    # base case
    if len(word) == 0:
        root.isTerminal = True
        return

    ch = word[0]
    index = ord(ch) - ord('a')
    # present
    if root.children[index] is not None:
        child = root.children[index]
    else:
        # not present
        child = TrieNode(ch)
        root.childCount += 1   # new line added
        root.children[index] = child

    # recursion sambhal lega
    insertWord(child, word[1:])

def findLCP(first, root):
    ans = ""
    # yha main galti karunga
    if root.isTerminal:
        return ""                    # CodeHelp only return

    for ch in first:
        if root.childCount == 1:
            ans += ch
            index = ord(ch) - ord('a')
            root = root.children[index]
        else:
            break

        if root.isTerminal:
            break

    return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # strs = ["flower","flow","flight"]
        if not strs:
            return ""  # Return empty string for empty input

        root = TrieNode('-')
        # insert strings
        for word in strs:
            insertWord(root, word)

        first = strs[0]
        ans = findLCP(first, root)
        return ans




# class TrieNode:
#     def __init__(self, d):
#         self.data = d
#         self.children = [None] * 26
#         self.isTerminal = False

# def insertWord(root, word):
#     # base case
#     if len(word) == 0:
#         root.isTerminal = True
#         return

#     ch = word[0]
#     index = ord(ch) - ord('a')
#     # present
#     if root.children[index] is not None:
#         child = root.children[index]
#     else:
#         # not present
#         child = TrieNode(ch)
#         root.children[index] = child

#     # recursion sambhal lega
#     insertWord(child, word[1:])

# def searchWord(root, word):
#     # base case
#     if len(word) == 0:
#         return root.isTerminal

#     ch = word[0]
#     index = ord(ch) - ord('a')
#     # present
#     if root.children[index] is not None:
#         child = root.children[index]
#     else:
#         return False

#     # rec call
#     return searchWord(child, word[1:])

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str: # strs = ["flower","flow","flight"]
#         ans = ""
#         # Loop on first string
#         for i in range(len(strs[0])):
#             ch = strs[0][i]
#             match = True

#             # Compare this character with all
#             # the remaining strings at the same index
#             for j in range(1, len(strs)):
#                 # Compare
#                 if len(strs[j]) < i+1 or ch != strs[j][i]:
#                     match = False
#                     break

#             if not match:
#                 break
#             else:
#                 ans += ch

#         return ans





        # ans = ""
        # i = 0
        # while(True):
        #     curr_ch = 0
        #     for strr in strs:
        #         if i >= len(strr):
        #             # out of Bound
        #             curr_ch = 0
        #             break
                
        #         # just started
        #         if curr_ch == 0:
        #             curr_ch = strr[i]

        #         elif strr[i] != curr_ch:
        #             curr_ch = 0
        #             break

        #     if curr_ch == 0:
        #         break
            
        #     ans += curr_ch
        #     i += 1

        # return ans























        # short = min(strs, key=len) # short = "flow"
        # for item in strs: # When item = "flight"
        #     while len(short) > 0:
        #         if item.startswith(short): # during loop 1 condition fails, during loop 2 condition fails, during loop 3 "flight" startswith fl is True
        #             break
        #         else:
        #             short = short[:-1] # during loop 1 short = flo, during loop 2 short = fl
        # return short