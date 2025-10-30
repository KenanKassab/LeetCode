from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def longestSubarray(nums, limit):
            max_dq, min_dq = deque(), deque()
            left = 0
            res = 0

            for right, num in enumerate(nums):
                while max_dq and num > max_dq[-1]:
                    max_dq.pop()
                max_dq.append(num)

                while min_dq and num < min_dq[-1]:
                    min_dq.pop()
                min_dq.append(num)

                while max_dq[0] - min_dq[0] > limit:
                    if nums[left] == max_dq[0]:
                        max_dq.popleft()
                    if nums[left] == min_dq[0]:
                        min_dq.popleft()
                    left += 1

                res = max(res, right - left + 1)

            return res
        return longestSubarray(nums, limit)

        

        
