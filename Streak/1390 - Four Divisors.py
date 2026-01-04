import math 
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        Ans = 0
        for num in nums:
            l = math.ceil(math.sqrt(num))
            T = []
            for i in range(1,l+1):
                if num % i == 0:
                    T.append(i) 
                    T.append(num/i)
            
            if len(set(T)) == 4:
                Ans += int(sum(set(T)))
        return Ans
