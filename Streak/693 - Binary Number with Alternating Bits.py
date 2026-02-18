class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        flag = True
        for i in range(3,len(s)):
            if s[i] == s[i-1]:
                flag = False
                break
        
        return flag
