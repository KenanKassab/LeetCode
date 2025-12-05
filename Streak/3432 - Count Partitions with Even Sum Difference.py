class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        S = sum(nums)
        n = len(nums)
        ans = 0
        L = 0
        for i in range(n-1):
            L += nums[i]
            R = S - L
            if abs(R - L) % 2 == 0:
                ans += 1

        return ans

