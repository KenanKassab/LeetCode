class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        idx1 = nums.index(min(nums))
        idx2 = -1
        temp = 1e5
        for i in range(len(nums)):
            if nums[i] < temp and i != idx1:
                idx2 = i
                temp = nums[i]

        
        n = len(nums)
        t1 = min(idx1,idx2)
        t2 = max(idx1,idx2)
        # print(t1,t2)
        if t1 == 0 and t2 == n-1:
            ans = nums[t1] + nums[t2] + min(nums[t1+1:t2])
        elif t1 == 0:
            ans = nums[t1] + nums[t2] + min(nums[t1+1:t2] + nums[t2+1:])
        else:
            ans = nums[0] + nums[t1] + nums[t2]

        return ans
