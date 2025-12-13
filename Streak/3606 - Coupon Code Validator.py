import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = r'^[a-zA-Z0-9_]+$'
        A = ["electronics", "grocery", "pharmacy", "restaurant"]
        D = {"electronics" : [], 
                "grocery" : [],
                "pharmacy" : [],
                "restaurant" : []}
        n = len(code)
        Ans = []
        for i in range(n):
            if isActive[i]:
                if businessLine[i] in A:
                    if re.match(pattern, code[i]):
                        D[businessLine[i]].append(code[i])

        for k ,v in D.items():
            for i in sorted(v):
                Ans.append(i)
        return Ans
