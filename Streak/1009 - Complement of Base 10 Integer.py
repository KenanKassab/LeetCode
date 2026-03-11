class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)
        ans = ['0', 'b']
        for i in x[2:]:
            if i == '0':
                ans.append('1')
            else:
                ans.append('0')
        temp = ''.join(ans)
        return int(temp,2)
