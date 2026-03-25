class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        R = [0 for i in range(n)]
        C = [0 for i in range(m)]

        for i in range(n):
            temp = 0
            for j in range(m):
                C[j] += grid[i][j]
                temp += grid[i][j]
            R[i] = temp

        sum_R = sum(R)
        sum_C = sum(C)

        temp = 0
        for i in range(len(R)):
            temp += R[i]
            if temp == sum_R - temp:
                return True

        temp = 0
        for i in range(len(C)):
            temp += C[i]
            if temp == sum_C - temp:
                return True

        return False
