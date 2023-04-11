# https://leetcode.com/problems/combination-sum-ii/

def combinationSumHelper(candidates, target, a, ans, index):
    # base
    if target == 0: 
        ans.append(a[:])
        return
    if target < 0: return

    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:                        #
            continue                                                                # Optimized
        a.append(candidates[i])
        combinationSumHelper(candidates, target - candidates[i], a, ans, i + 1)
        a.pop()


class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans, a = [], []
        combinationSumHelper(candidates, target, a, ans, 0)
        # st = set()
        # for e in ans:
        #     st.add(tuple(e))               cause TLE
        # ans.clear()
        # for e in st:
        #     ans.append(list(e)) # only unique 
        return ans