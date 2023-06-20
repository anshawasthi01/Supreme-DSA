# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/description/

#CodeHelp
#sort every list and sort on the basis of width then LIS (W, L, H)

class Solution:
    def check(self, a, b):
        if b[0] <= a[0] and b[1] <= a[1] and b[2] <= a[2]:
            return True
        else:
            return False

    def solveUsingTabSO(self, arr):
        n = len(arr)
        # dp = [[0] * (n+1) for _ in range(n+1)]
        currRow = [0] * (n+1)
        nextRow = [0] * (n+1)

        for curr in range(n-1, -1, -1):
            for prev in range(curr - 1, -2, -1):
                # include
                include = 0
                if prev == -1 or self.check(arr[curr], arr[prev]):
                    include = arr[curr][2] + nextRow[curr + 1]

                # exclude
                exclude = 0 + nextRow[prev + 1]

                currRow[prev + 1] = max(include, exclude)
            # shift
            nextRow = currRow.copy()
        return nextRow[0]

    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # sort every array
        for a in cuboids:
            a.sort()

        # sort the 2D array
        cuboids.sort()

        # apply lis logic
        ans = self.solveUsingTabSO(cuboids)
        return ans

