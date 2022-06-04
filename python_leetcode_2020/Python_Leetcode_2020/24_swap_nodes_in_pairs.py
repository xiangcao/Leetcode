"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Recursive
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        third = self.swapPairs(head.next.next)
        tmp = head
        head = head.next
        head.next = tmp
        head.next.next = third
        return head

    # Iterative
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next       
