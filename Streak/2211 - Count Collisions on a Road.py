class Solution:
    def countCollisions(self, directions: str) -> int:
        R = 0
        L = 0
        S = 0
        n = len(directions)
        ans = 0
        for i in range(n):
            if directions[i] == 'L':
                ans += R
                R = 0
            elif directions[i] == 'R':
                R += 1
            else:
                ans += R
                R = 0
        
        print(ans)
        R = 0
        L = 0
        S = 0
        for i in range(n-1,-1,-1):
            if directions[i] == 'R':
                ans += L
                L = 0
            elif directions[i] == 'L':
                L += 1
            else:
                ans += L
                L = 0

        return ans

