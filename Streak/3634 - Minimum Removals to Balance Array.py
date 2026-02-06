class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        A = sorted(nums)
        n = len(A)
        if len(A) == 1:
            return 0

        print(A)
        r = 0
        ans = n
        temp = 0
        for l in range(n):
            while r < n and A[r] <= A[l]*k:
                r += 1
            
            ans = min(ans, n - (r - l))
        
        return ans
            
