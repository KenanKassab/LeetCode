class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        idx = -1
        if digits[-1] == 9:
            i = n-1
            while i >= 0 and digits[i] == 9:
                idx = i
                i -= 1
        
            if idx == 0:
                Ans = [1]
                for i in range(n):
                    Ans.append(0)
            else:
                Ans = []
                for i in range(n):
                    if i == idx - 1:
                        Ans.append(digits[i] + 1)
                    elif i >= idx:
                        Ans.append(0)
                    else:
                        Ans.append(digits[i])
            
            return Ans

        else:
            Ans = digits[:-1]
            Ans.append(digits[-1] + 1)
            return Ans

