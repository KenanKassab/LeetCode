# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}

        idx = 0
        while head:
            if head.next == None:
                return None

            if head in visited.keys():
                return visited[head]
            
            visited[head] = head
            idx += 1
            head = head.next
        
