class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        A = [s[i] for i in range(len(s))]
        while len(A) > 1:
            if A[-1] == '0':
                A = A[:-1]
                ans += 1
            else:
                idx = -1
                while abs (idx) <= len(A) and A[idx] == '1':
                    A[idx] = '0'
                    idx -= 1

                try:
                    A[idx] = '1'
                except:
                    A = ['1'] + A
                ans += 1

        return ans


