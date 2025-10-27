class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        new_nums = []
        for item in nums:
            if item == 0:
                new_nums.append(-1)
            else:
                new_nums.append(1)
        
        prefix = []
        s = 0
        for item in new_nums:
            s+=item
            prefix.append(s)
        
        ans = 0
        seen = {0:-1}
        for i in range(len(prefix)):
            if prefix[i] in seen:
                ans = max(ans,i-seen[prefix[i]])
            else:
                seen[prefix[i]] = i
        
        return ans
        
        

        
        
        



