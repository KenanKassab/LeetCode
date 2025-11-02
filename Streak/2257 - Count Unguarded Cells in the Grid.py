class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = -1
        for r, c in walls:
            grid[r][c] = -2

        for r in range(m):
            seen_guard = False
            for c in range(n):
                if grid[r][c] == -1:        
                    seen_guard = True 
                elif grid[r][c] == -2:
                    seen_guard = False
                elif seen_guard:
                    grid[r][c] = 1

            seen_guard = False
            for c in range(n-1, -1, -1):
                if grid[r][c] == -1:        
                    seen_guard = True 
                elif grid[r][c] == -2:
                    seen_guard = False
                elif seen_guard:
                    grid[r][c] = 1


        for c in range(n):
            seen_guard = False
            for r in range(m):
                if grid[r][c] == -1:        
                    seen_guard = True 
                elif grid[r][c] == -2:
                    seen_guard = False
                elif seen_guard:
                    grid[r][c] = 1

            seen_guard = False
            for r in range(m-1, -1, -1):
                if grid[r][c] == -1:        
                    seen_guard = True 
                elif grid[r][c] == -2:
                    seen_guard = False
                elif seen_guard:
                    grid[r][c] = 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1

        return ans
