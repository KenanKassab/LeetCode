class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        A = sorted(happiness)
        c = 0
        ans = 0
        for i in range(len(A)-1,-1,-1):
            if c == k:
                break
            ans += max(A[i] - c, 0)
            c += 1
            

        return ans
