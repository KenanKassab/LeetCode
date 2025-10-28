class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                pos.append(i)
        
        e = 0
        ans = 0
        for idx in pos:
            if sum(nums[:idx]) == sum(nums[idx:]):
                e += 1
            elif abs(sum(nums[:idx]) - sum(nums[idx:])) == 1:
                ans += 1
        
        return ans + e*2
