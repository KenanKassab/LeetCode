class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        A = [2,3,5,7,11,13,17,19]
        ans = 0
        for i in range(left, right + 1):
            s = bin(i)[2:]
            temp = s.count('1')
            if temp in A:
                # print(i)
                ans += 1
        
        return ans
