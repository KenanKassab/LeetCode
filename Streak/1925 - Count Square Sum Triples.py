import math 
class Solution:
    def countTriples(self, n: int) -> int:
        d = {}
        ans = 0
        for i in range(1,n):
            for j in range(1,n):
                aa = math.sqrt(j**2 + i**2)
                if aa.is_integer() and aa <= n :
                    ans += 1

        return ans
