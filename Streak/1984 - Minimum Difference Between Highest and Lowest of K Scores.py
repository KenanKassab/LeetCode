class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        A = sorted(nums)
        ans = 1e9
        # print(A)
        for i in range(len(nums)-k+1):
            # print(A[i], A[i+k-1])
            temp = A[i+k-1] - A[i]
            if temp < ans:
                ans = temp
            


        return ans

