# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1->2 move to right by 3 places? 
        # [1], 1
        # [1,2], 0
        # [1], 0
        
        # use fast and slow pointer
        if not head or not k:
            return head
            
        fast = slow = head
        
        length = 0 
        p = head
        while p:
            p = p.next
            length += 1
        k = k % (length)
        if not k:
            return head
        while fast and k:
            k -= 1
            fast = fast.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        newhead = slow.next
        slow.next = None
        return newhead
    
        
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # no use of fast/slow pointer
        # refer https://leetcode.com/discuss/36706/my-clean-code-quite-standard-find-tail-and-reconnect-the-list
