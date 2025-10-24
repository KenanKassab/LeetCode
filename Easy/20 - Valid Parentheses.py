class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for ch in s:
            if ch == "(" or  ch == "{" or  ch == "[" :
                a.append(ch)
            elif a == []:
                a.append(ch)
            elif ch == ")" and a[-1] == "(":
                a.pop()
            elif ch == "}" and a[-1] == "{":
                a.pop()
            elif ch == "]" and a[-1] == "[":
                a.pop()
            else:
                a.append(ch)
        
        if a == []:
            return True
        else:
            return False
        