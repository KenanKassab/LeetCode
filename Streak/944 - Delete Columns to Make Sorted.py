class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        Ans = 0
        for i in range(m):
            for j in range(1, n):
                if strs[j][i] < strs[j-1][i]:
                    Ans += 1
                    break

        return Ans
