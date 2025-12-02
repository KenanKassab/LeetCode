class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = {}
        MOD = 10**9 + 7
        for p in points:
            x = p[0]
            y = p[1]
            d[y] = d.get(y, 0) + 1

        A = []
        for k, v in d.items():
            if v < 2:
                continue
            temp = (v * (v-1))//2
            A.append(temp % MOD)

        ans = 0
        S = sum(A) % MOD
        S2 = sum((x * x) % MOD for x in A) % MOD

        ans = (S * S - S2) % MOD
        inv2 = pow(2, MOD-2, MOD)
        ans = ans * inv2 % MOD

        return int(ans)
