class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        dp = {}
        n = len(grid)
        m = len(grid[0])
        dp = [[0,0,0]] * m
        # print(dp)
        ans = 0
        for i in range(n):
            row_sum = [0,0,0]
            for j in range(m):
                if grid[i][j] == 'X':
                    temp = [dp[j][0] + 1, dp[j][1], dp[j][2]]
                    dp[j] = temp
                    row_sum[0] += dp[j][0]
                    row_sum[1] += dp[j][1]
                    row_sum[2] += dp[j][2]

                elif grid[i][j] == 'Y':
                    temp = [dp[j][0], dp[j][1] + 1, dp[j][2]]
                    dp[j] = temp
                    row_sum[0] += dp[j][0]
                    row_sum[1] += dp[j][1]
                    row_sum[2] += dp[j][2]

                else:
                    temp = [dp[j][0], dp[j][1], dp[j][2] + 1]
                    dp[j] = temp
                    row_sum[0] += dp[j][0]
                    row_sum[1] += dp[j][1]
                    row_sum[2] += dp[j][2]

                if row_sum[0] == row_sum[1] and row_sum[0] != 0:
                    # print(row_sum)
                    # print(dp)
                    ans+= 1
        return ans

