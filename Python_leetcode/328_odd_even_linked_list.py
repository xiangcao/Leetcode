# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        evenhead = head.next
        p1, p2 = head, head.next
        while p2 and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = evenhead
        return head
