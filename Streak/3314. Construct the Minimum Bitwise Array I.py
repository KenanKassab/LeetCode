class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        Ans = []
        for num in nums:
            flag = False
            for i in range(num):
                if i | i + 1 == num:
                    Ans.append(i)
                    flag = True
                    break
            if not flag:
                Ans.append(-1)
        
        return Ans



