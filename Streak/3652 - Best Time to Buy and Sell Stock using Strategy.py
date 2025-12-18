class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        S = 0
        C = [0 for i in range(n+1)]
        Ans = 0
        O = [0]
        P = [0]
        tt = 0
        for i in range(n):
            Ans += prices[i] * strategy[i]
            tt += prices[i]
            P.append(tt)
            O.append(Ans)

        for i in range(n-1,-1,-1):
            S += prices[i] * strategy[i]
            C[i] = S

        
        for i in range(n-k+1):
            idx = k//2 
            # temp = sum(prices[i + idx :i + k])
            temp = P[i+k] - P[i+idx]
            # print(temp)
            if O[i] + temp + C[i + k] > Ans:
                Ans = O[i] + temp + C[i + k]

        return Ans
