class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        Ans = []
        n = len(nums)
        for i in range(n):
            step = nums[i]
            if step > 0:
                temp = (i + abs(step)) % n
                Ans.append(nums[temp])
            elif step < 0:
                temp = i - (abs(step) % n)
                Ans.append(nums[temp])
            else:
                Ans.append(nums[i])
        return Ans
