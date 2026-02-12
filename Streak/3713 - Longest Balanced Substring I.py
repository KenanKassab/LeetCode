class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            d = {}
            for j in range(i, n):
                d[s[j]] = d.get(s[j],0) + 1
                # print(d)
                if len(set(d.values())) == 1:
                    # print(d.values())
                    ans = max(ans, sum(d.values()))
        
        return ans
