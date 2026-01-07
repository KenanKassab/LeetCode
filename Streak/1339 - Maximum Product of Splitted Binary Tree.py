# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def traverse(s):
            if not s :
                # print("HI")
                return 0
            
            if s in dp:
                return dp[s]
            # print(s.val)
            dp[s] = s.val + traverse(s.left) + traverse(s.right)
            return dp[s]

        total_sum = traverse(root)
        
        ans = 0

        def find_max(s):
            nonlocal ans
            if not s:
                return 

            temp = dp[s]
            curr_mul = (temp * (total_sum - temp))
            if curr_mul > ans:
                ans = curr_mul

            find_max(s.left)
            find_max(s.right)
        
        find_max(root)
        return ans % (10**9 + 7)
        
            
