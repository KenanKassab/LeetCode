"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        D = {}
        current = head
        while current is not None:
            D[current] = Node(current.val)
            current = current.next

        current = head
        while current is not None:
            D[current].next = D.get(current.next)
            D[current].random = D.get(current.random)
            current = current.next


        return D[head]
