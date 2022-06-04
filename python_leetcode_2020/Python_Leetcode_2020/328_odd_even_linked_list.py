# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd_head, even_head = head, head.next
        p, q = odd_head, even_head
        while q and q.next:
            p.next = q.next
            p = p.next
            q.next = p.next
            q = q.next
        p.next = even_head
        return odd_head
