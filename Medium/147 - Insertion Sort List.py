# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        sorted_list = ListNode()
        sorted_list.next = head

        last_sorted = head
        curr = head.next
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = curr

            else:
                p = sorted_list
                while p.next.val < curr.val:
                    p = p.next

                last_sorted.next = curr.next

                curr.next = p.next
                p.next = curr
            curr = last_sorted.next
        
        return sorted_list.next

