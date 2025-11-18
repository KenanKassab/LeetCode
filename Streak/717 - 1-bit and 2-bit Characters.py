class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        print(n)
        if n == 1:
            return True
        
        if n == 2:
            if bits[0] == 1:
                return False
            else:
                return True

        if bits[n-2] == 0:
            return True

        # print("asdasdas")
        i = 0
        while True:
            # print(i)
            if i == n-2:
                return False
            
            if i > n-2:
                return True

            if bits[i] == 0:
                i += 1
            else:
                i += 2
