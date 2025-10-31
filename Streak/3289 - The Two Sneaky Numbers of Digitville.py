class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for num in nums:
            if num in d.keys():
                ans.append(num)
            else:
                d[num] = 1
        
        return ans
