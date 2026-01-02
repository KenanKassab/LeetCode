class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            if num in visited:
                return num
            visited[num] = 1
