class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 1e7
        temp = 0
        count = 0
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    count += 1
                temp += abs(matrix[i][j])
                if abs(matrix[i][j]) < s:
                    s = abs(matrix[i][j])

        if count % 2 == 0:
            return temp
        else:
            return temp - 2*s
