class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        def numberOfPaths(grid, k):
            MOD = 10**9 + 7
            m, n = len(grid), len(grid[0])
            
            # dp[i][j][r] = number of ways to reach (i,j) with remainder r
            dp = [[[0] * k for _ in range(n)] for _ in range(m)]
            
            # base case
            start_r = grid[0][0] % k
            dp[0][0][start_r] = 1

            for i in range(m):
                for j in range(n):
                    val_r = grid[i][j] % k

                    # skip the start cell
                    if i == 0 and j == 0:
                        continue

                    # from top
                    if i > 0:
                        for r in range(k):
                            prev = dp[i-1][j][r]
                            if prev:
                                dp[(i)][j][(r + val_r) % k] = (dp[i][j][(r + val_r) % k] + prev) % MOD

                    # from left
                    if j > 0:
                        for r in range(k):
                            prev = dp[i][j-1][r]
                            if prev:
                                dp[i][j][(r + val_r) % k] = (dp[i][j][(r + val_r) % k] + prev) % MOD

            return dp[m-1][n-1][0]

        return numberOfPaths(grid, k)

