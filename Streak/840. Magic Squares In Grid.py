class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_is_magic(A):
            N = []
            R = []
            C = []
            for i in range(3):
                temp = 0
                temp2 = 0
                for j in range(3):
                    N.append(A[i][j])
                    temp += A[i][j]
                    temp2 += A[j][i]
                R.append(temp)
                C.append(temp2)

            if len(set(N)) != 9 or sum(N) != 45:
                return 0

            for i in range(1, 10):
                if i not in (N):
                    return 0

            D = sum([A[i][i] for i in range(3)])
            RD = sum([A[i][2-i] for i in range(3)])
            if D != RD:
                return 0
            
            for item in R:
                if item != D:
                    return 0
            
            for item in C:
                if item != D:
                    return 0

            return 1

        
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0

        ans = 0
        for i in range(n-2):
            for j in range(m-2):
                A = [row[j:j+3] for row in grid[i:i+3]]
                ans += check_is_magic(A)


        return ans


