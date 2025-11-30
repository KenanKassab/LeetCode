class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s % p == 0:
            return 0

        need = s % p
        prefix = []
        temp = 0
        for num in nums:
            temp += num
            prefix.append(temp)

        M = {0 : -1}
        res = len(nums)
        for i in range(len(nums)):
            curr_mod = (prefix[i]%p - need + p) % p
            if curr_mod in M:
                res = min(res, abs(M[curr_mod] - i))
            
            M[prefix[i]%p] = i

        return res if res < len(nums) else -1
            
