# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visted = []
        def find_cycle(node):
            
            if not node:
                return False

            if node in visted:
                return True
                
            visted.append(node)
            return find_cycle(node.next)

        return find_cycle(head)
