class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}

        def match(i,j):
            if i >= len(nums1) or j>= len(nums2):
                return float("-inf")
            
            if (i,j) in dp:
                return dp[(i,j)]

            temp = nums1[i] * nums2[j]
            dp[(i,j)] = max(temp, temp + match(i+1,j+1), match(i + 1, j), match(i, j+1))
            return dp[(i,j)]

        return match(0,0)
