class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans = {}
        def solve(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l,r) in ans.keys():
                return ans[(l,r)]

            if s[l] == s[r]:
                ans[(l,r)] = 2 + solve(l+1, r-1)
            else:
                ans[(l,r)] = max(solve(l+1, r), solve(l, r-1))

            return ans[(l,r)]       

        return solve(0, len(s)-1)
