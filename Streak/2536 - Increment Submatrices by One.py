class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0]* (n+1) for i in range(n+1)]

        for query in queries:
            row1 = query[0]
            col1 = query[1]
            row2 = query[2]
            col2 = query[3]

            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1

            
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c-1]

        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r-1][c]

        final_mat = [row[:n] for row in diff[:n]]

        
        return final_mat
