class Solution:
    def maxSumDivThree(self, nums):
        dp = [0, float('-inf'), float('-inf')]
        
        for x in nums:
            new_dp = dp[:]
            r = x % 3
            for prev_r in range(3):
                new_r = (prev_r + r) % 3
                new_dp[new_r] = max(new_dp[new_r], dp[prev_r] + x)
            dp = new_dp
        
        return dp[0]

