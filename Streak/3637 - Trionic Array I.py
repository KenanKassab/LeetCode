class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        flag = False
        n = len(nums)
        if n == 3:
            return False
        count = 0
        flag == 0
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return False

            if nums[i] > nums[i-1]:
                if flag == 1:
                    continue
                else:
                    count += 1
                    flag = 1
            
            elif nums[i] < nums[i-1]:
                if flag == -1:
                    continue
                else:
                    count += 1
                    flag = -1

        # print(count, flag)
        if count == 3 and flag == 1:
            return True
        else:
            return False

            

            
        
