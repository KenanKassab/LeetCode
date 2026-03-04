class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        R = []
        C = []
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            temp = 0 
            for j in range(m):
                temp += mat[i][j]
            R.append(temp)

        for j in range(m):
            temp = 0 
            for i in range(n):
                temp += mat[i][j]
            C.append(temp)

        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if R[i] == 1 and C[j] == 1:
                        ans += 1
            

        return ans
