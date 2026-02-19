class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        temp = 1
        A = []
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                temp += 1
            else:
                A.append(temp)
                temp = 1
        A.append(temp)
        # print(A)

        ans = 0

        for i in range(1,len(A)):
            ans += min(A[i],A[i-1])
        
        return ans
