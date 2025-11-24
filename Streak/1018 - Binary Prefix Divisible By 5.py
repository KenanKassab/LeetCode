class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = 0
        R = []
        for i in range(n):
            if nums[i] == 1:
                ans += 2**(n-i)
            
            if ans % 5 == 0:
                R.append(True)
            else:
                R.append(False)

        return R
        
