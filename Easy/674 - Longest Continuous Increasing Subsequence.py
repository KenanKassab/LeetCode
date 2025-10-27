class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] <= 0:
                ans = max(ans, count)
                count = 1
            else:
                count += 1
        ans = max(ans, count)
        
        return ans
        
