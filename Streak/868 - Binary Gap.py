class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)
        temp = 0
        A = []
        for i in range(2,len(s)):
            if s[i] == '1':
                A.append(temp)
                temp = 0
            else:
                temp += 1
        # print(s)
        # print(A)
        ans = max(A)
        if len(A) == 1:
            return 0
        else:
            return ans + 1
