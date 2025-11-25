class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1
        digits = 1
        # print (1 % 3)

        while True:
            # print(n)
            if n % k == 0 :
                return digits
            
            if digits > k:
                return -1 
                break

            n *= 10
            n += 1
            digits += 1
