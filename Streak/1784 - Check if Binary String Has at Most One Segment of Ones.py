class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        L = []
        temp = 1
        if s[0] == '1':
            temp = 1
        else:
            temp = 0
        for i in range(1, len(s)):
            if s[i] == '1' and s[i] == s[i-1]:
                temp += 1
            elif s[i] == '1':
                temp = 1
            else:
                if temp >= 1:
                    L.append(temp)
                temp = 0
        if temp >= 1:
            L.append(temp)
        # print(L)
        if len(L) == 1:
            return True
        return False
