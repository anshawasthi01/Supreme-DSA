class Solution:
    # index = index  of last element
    def solveUsingRecursion(self, weight, value, index, capacity):
        # base case -> only 1 item
        if index == 0:
            if weight[0] <= capacity:
                return value[0]
            else:
                return 0

        # include and exclude
        include = 0
        if weight[index] <= capacity:
            include = value[index] + self.solveUsingRecursion(weight, value, index-1, capacity - weight[index])

        exclude = 0 + self.solveUsingRecursion(weight, value, index-1, capacity)

        return max(include, exclude)

    def solveUsingMem(self, weight, value, index, capacity, dp):
        # base case -> only 1 item
        if index == 0:
            if weight[0] <= capacity:
                return value[0]
            else:
                return 0

        if dp[index][capacity] != -1:
            return dp[index][capacity]

        # include and exclude
        include = 0
        if weight[index] <= capacity:
            include = value[index] + self.solveUsingMem(weight, value, index-1, capacity - weight[index], dp)

        exclude = 0 + self.solveUsingMem(weight, value, index-1, capacity, dp)

        dp[index][capacity] = max(include, exclude)
        return dp[index][capacity]

    def solveUsingTabulation(self, weight, value, n, capacity):
        dp = [[0] * (capacity+1) for _ in range(n)]

        for w in range(weight[0], capacity+1):
            if weight[0] <= capacity:
                dp[0][w] = value[0]
            else:
                dp[0][w] = 0

        for index in range(1, n):
            for wt in range(capacity+1):
                # include and exclude
                include = 0
                if weight[index] <= wt:
                    include = value[index] + dp[index-1][wt - weight[index]]

                exclude = 0 + dp[index-1][wt]

                dp[index][wt] = max(include, exclude)

        return dp[n-1][capacity]

    def solveUsingSO(self, weight, value, n, capacity):
        prev = [0] * (capacity+1)
        curr = [0] * (capacity+1)

        for w in range(weight[0], capacity+1):
            if weight[0] <= capacity:
                prev[w] = value[0]
            else:
                prev[w] = 0

        for index in range(1, n):
            for wt in range(capacity+1):
                # include and exclude
                include = 0
                if weight[index] <= wt:
                    include = value[index] + prev[wt - weight[index]]

                exclude = 0 + prev[wt]

                curr[wt] = max(include, exclude)
            
            # shift
            prev = curr[:]
        
        return prev[capacity]

    def solveUsingSO2(self, weight, value, n, capacity):
        curr = [0] * (capacity+1)

        for w in range(weight[0], capacity+1):
            if weight[0] <= capacity:
                curr[w] = value[0]
            else:
                curr[w] = 0

        for index in range(1, n):
            for wt in range(capacity, -1, -1):
                # include and exclude
                include = 0
                if weight[index] <= wt:
                    include = value[index] + curr[wt - weight[index]]

                exclude = 0 + curr[wt]

                curr[wt] = max(include, exclude)

        return curr[capacity]


if __name__ == "__main__":
    weight = [4, 5, 1]
    value = [1, 2, 3]
    n = 3
    capacity = 4

    sol = Solution()

    # ans = sol.solveUsingRecursion(weight, value, n - 1, capacity)

    # dp = [[-1] * (capacity + 1) for _ in range(n)]
    # ans = sol.solveUsingMem(weight, value, n - 1, capacity, dp)

    # ans = sol.solveUsingSO(weight, value, n, capacity)

    ans = sol.solveUsingSO2(weight, value, n, capacity)
    print("Ans:", ans)
