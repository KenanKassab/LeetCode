class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = []
        for row in bank:
            s = 0
            for c in row:
                if c == '1':
                    s+=1
            if s == 0:
                continue
            ans.append(s)
        # print(ans)
        if len(ans) == 1:
            return 0
        else:
            l = 0
            for i in range(len(ans) - 1):
                l += ans[i] * ans[i+1]
            return l
        # print(ans)

