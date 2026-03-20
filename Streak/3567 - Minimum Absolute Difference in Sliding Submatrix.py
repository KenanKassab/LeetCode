class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def find_min(A):
            
            temp = 10**11
            M = list(set([val for row in A for val in row]))
            if len(M) == 1:
                return 0
            # print(M)
            for i in range(len(M)):
                for j in range(i+1,len(M)):
                    if abs(M[i] - M[j]) < temp:
                        temp = abs(M[i] - M[j]) 

            # print(temp)
            return temp

        n = len(grid)
        m = len(grid[0])
        # print(n,m,k)
        Ans = [[0]*(m-k+1) for i in range(n-k+1)]

        # print(Ans)
        for i in range(n-k+1):
            for j in range(m-k+1):
                A = [row[j:j+k] for row in grid[i:i+k]]
                # print(A, i, j)
                # print(i,j)
                Ans[i][j] = find_min(A)

        return Ans

