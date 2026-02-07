class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return 0
        A = [0]
        B = [0]
        temp_a = 0
        temp_b = 0
        for i in range(n):
            if s[i] == 'a':
                temp_a += 1
                A.append(temp_a)
                B.append(temp_b)
            else:
                temp_b += 1
                A.append(temp_a)
                B.append(temp_b)

        ans = 1e9
        # print(A)
        # print(B)
        for i in range(n+1):
            l_b = B[i] - B[0]
            r_a = A[-1] - A[i]
            # print (i,l_b, r_a)
            temp_ans = l_b + r_a
            ans = min(ans,temp_ans)

        return ans

