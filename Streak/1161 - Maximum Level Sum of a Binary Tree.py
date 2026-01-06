# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dp = {}
        def traverse(s, count):
            if not s:
                return
            
            if s.left:
                dp[count] = dp.get(count, 0) + s.left.val
            if s.right:
                dp[count] = dp.get(count, 0) + s.right.val

            # dp[count] = temp
            traverse(s.left, count + 1)
            traverse(s.right, count + 1)
        
        dp[1] = root.val
        traverse(root, 2)
        l = -1
        ans = -1e7
        for k,v in dp.items():
            if v > ans:
                ans = v
                l = k
        print(dp)
        return l
        
        
