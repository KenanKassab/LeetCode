# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = []
        while head:
            L.append(head.val)
            head = head.next
        L = sorted(L)
        sorted_list = ListNode()
        dummy = sorted_list
        for node in L:
            dummy.next = ListNode(node)
            dummy = dummy.next

        # print(sorted_list)
        return sorted_list.next

        
