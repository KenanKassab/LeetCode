class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        I = [int(i,2) for i in nums]
        # print(I)
        for i in range(n+2):
            if i not in I:
                # print(i)
                s = bin(i)
                return s[2:].zfill(n)


