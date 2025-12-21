class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A) - 1))

        n = len(strs)
        m = len(strs[0])
        Ans = ["" for i in range(n)]
        count = 0
        for i in range(m):
            A = []
            for j in range(n):
                Ans[j] += strs[j][i]

            if is_sorted(Ans):
                continue
            else:
                count += 1
                for k in range(n):
                    Ans[k] = Ans[k][:-1]
                
            
        # print(Ans)
        return count
