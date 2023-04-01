# https://leetcode.com/problems/wildcard-matching/

# CodeHelp
def isMatchHelper(s, si, p, pi):
    # base
    if si == len(s) and pi == len(p): return True

    if si == len(s) and pi < len(p):
        while pi < len(p):
            if p[pi] != '*': return False
            pi += 1
        return True

    # check bounds
    if si >= len(s) or pi >= len(p):
        return False

    # single char matching
    if (s[si] == p[pi]) or ('?' == p[pi]):
        return isMatchHelper(s, si+1, p, pi+1)

    if p[pi] == '*':
        # treat '*' as empty or null
        caseA = isMatchHelper(s, si, p, pi + 1)

        # let '*' sonsume one char
        caseB = isMatchHelper(s, si + 1, p, pi)
        return caseA or caseB

    # char doesn't matching
    return False

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        si = 0
        pi = 0
        return isMatchHelper(s, si, p, pi)
