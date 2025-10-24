class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        diff = r-l
        area = min(height[l], height[r]) * diff
        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            diff -= 1
            area = max(area, min(height[l], height[r]) * diff)
            
        return area

        
