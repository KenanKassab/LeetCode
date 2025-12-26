class Solution:
    def bestClosingTime(self, customers: str) -> int:
        idx = -1
        P = []
        n = len(customers)
        temp_N = 0
        temp_Y = 0
        N = [0]
        Y = [0]
        for i in range(n):
            if customers[i] == 'Y':
                temp_Y += 1
            Y.append(temp_Y)

            if customers[i] == 'N':
                temp_N += 1
            N.append(temp_N)


        ans = 1e6
        idx = -1
        # print(N)
        # print(Y)
        for i in range(n+1):
            if N[i] - N[0] + Y[n] - Y[i] < ans:
                idx = i
                ans = N[i] - N[0] + Y[n] - Y[i]
            # print(ans)

        return idx
        
            
