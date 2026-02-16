class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)
        temp = s[2:].zfill(32)
        return int(temp[::-1],2)

