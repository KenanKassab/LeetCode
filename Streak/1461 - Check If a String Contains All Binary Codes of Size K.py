class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = {}
        for i in range(len(s)- k + 1):
            sub = s[i:i+k]
            d[sub] = d.get(sub, 0) + 1
        
        # print(d)
        if len(d) == 2**k:
            return True
        else:
            return False
