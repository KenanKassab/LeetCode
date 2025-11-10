class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        last = -1
        for i, num in enumerate(nums):
            if num == 0:
                ans += len(stack)
                stack = []
                continue
            # print(stack)
            while stack and stack[-1] > num:  
                stack.pop()
                ans += 1
            
            if not stack or stack[-1] < num:
                stack.append(num)
        ans += len(stack)

        return ans
