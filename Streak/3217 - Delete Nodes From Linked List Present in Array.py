# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        a = set(nums)
        l = ListNode()
        d = l
        while head:
            if head.val in a:
                head = head.next
                continue
            d.next = head
            d = d.next
            head = head.next
        d.next = None
        # print(l)
        return l.next
