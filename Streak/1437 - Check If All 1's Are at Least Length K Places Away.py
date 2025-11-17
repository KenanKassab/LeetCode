class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        try:
            temp = nums.index(1)
        except:
            return True
        # print(temp)
        for i in range(temp + 1, len(nums)):
            # print(i - temp)
            if nums[i] == 1:
                if i - temp - 1 < k:
                    return False
                else:
                    temp = i


        return True

