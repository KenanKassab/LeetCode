# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Flag = True
        def traverse(node):
            if not node:
                print("ops")
                return 0

            ans_l = traverse(node.left)
            ans_r = traverse(node.right)

            if abs(ans_l-ans_r) > 1:
                self.Flag = False

            return max(ans_l, ans_r) + 1
        
        traverse(root)
        return self.Flag

            

