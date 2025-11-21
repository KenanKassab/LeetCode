class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = {}
        for ch in s:
            d[ch] = d.get(ch,0) + 1
        
        ans = 0
        n = len(s)
        for k, v in d.items():
            if v < 2:
                continue

            if v >= 3:
                ans += 1

            idx = [i for i, ch in enumerate(s) if ch == k]
            sub = s[idx[0]:idx[-1]]
            ans += len(set(sub)) - 1
   

        return ans
