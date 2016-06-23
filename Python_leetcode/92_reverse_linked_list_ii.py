# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        nodeBeforeTheSegment = None
        while n > 1:
            fast = fast.next
            if n == m:
                nodeBeforeTheSegment = slow
                slow = slow.next
                m -= 1
            n -= 1
        prev = fast.next
        
        while slow != fast:
            temp, slow.next, prev = slow.next, prev, slow
            slow = temp
        slow.next = prev
        if nodeBeforeTheSegment:
            nodeBeforeTheSegment.next = slow
            return head
        else:
            return slow
            
        
                
                
