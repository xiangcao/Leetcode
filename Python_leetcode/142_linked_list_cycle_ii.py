# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                p1 = head
                p2 = slow
                while p1 and p2:
                    if p1 == p2:
                        return p1
                    p1, p2 = p1.next, p2.next
        return None
        
        
