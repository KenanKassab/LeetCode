class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for item in nums:
            if item in d.keys():
                d[item] += 1
            else:
                d[item] = 1

        for k, v in d.items():
            if v == 1:
                return k
