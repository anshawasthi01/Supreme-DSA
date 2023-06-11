    dp = [[-1] * (capacity + 1) for _ in range(n)]
    ans = sol.solveUsingMem(weight, value, n - 1, capacity, dp)