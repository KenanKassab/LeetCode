class Solution:
    def minOperations(self, s: str) -> int:
        o1 = []
        o2 = []

        for i in range(len(s)):
            if i % 2 == 0:
                o1.append('0')
                o2.append('1')
            else:
                o1.append('1')
                o2.append('0')

        v1 = 0
        v2 = 0
        for i in range(len(s)):
            if s[i] != o1[i]:
                v1 += 1
            else:
                v2 += 1

        return min(v1,v2)
        
