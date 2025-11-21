class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        a = sorted(nums)
        for i in range(len(a)):
            if a[i] == ans:
                ans *= 2
        
        return ans
