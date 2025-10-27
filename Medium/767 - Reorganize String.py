import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) == 1:
            return s
        d = {}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        m = max(d.values())
        if len(s)%2 == 0 and m > len(s)/2:
            return ""
        
        if len(s)%2 == 1 and m > len(s)/2 + 1:
            return ""
         
        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        new_s = ""
        chars = list(d.keys())
        res = d[chars[0]] - d[chars[1]] - 1
        for _ in range(m):
            for k,v in d.items():
                if v == 0:
                    continue
                new_s += k
                d[k] -= 1
        if res <= 0:
            return new_s 
        new_s = new_s[:-res]
        ch = chars[0]

        idx = []
        for i in range(len(new_s) - 1):
            if new_s[i] != ch and new_s[i+1] != ch:
                idx.append(i+1)
        
        idx = sorted(idx, reverse=True)
        original_s = list(new_s)

        if idx != []:
            for i in range(res):
                original_s.insert(idx[i], ch)

        return "".join(original_s)
