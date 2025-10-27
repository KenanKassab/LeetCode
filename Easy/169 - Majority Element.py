class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for item in nums:
            d[item] = d.get(item,0)+1
        
        d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        return list(d.keys())[0]
