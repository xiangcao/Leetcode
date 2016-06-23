# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False
        
