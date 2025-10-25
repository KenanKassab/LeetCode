class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        def solve(l, r, idx):

            if idx >= len(s):
                ans.append(s[l:r])
                return

            a = s[l:idx]
            b = s[idx:r]
            # print(a, b)
            if set(a) & set(b):
                solve(l, r, idx + 1)
            else:
                ans.append(a)
                solve(idx, r, idx + 1)
        solve(0, len(s), 1)
        k = [len(item) for item in ans]
        return k
