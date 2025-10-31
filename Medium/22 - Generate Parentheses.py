class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = "("
        Ans = []
        limit = n*2
        def generate(temp, l, r):
            if l == r and l + r == limit:
                Ans.append(temp)
                return temp

            if r > l or r + l >= limit:
                return ""
            
            
            generate(temp + "(", l + 1, r)
            generate(temp + ")", l , r + 1)

        generate("(", 1, 0)
        return Ans
