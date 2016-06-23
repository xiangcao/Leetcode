# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reverse and then compare? oh no. o(1) space!
        if not head or not head.next:
            return True
        slow = quick = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
        #reverse the nodes after slow
        p = slow.next
        prev = None
        while p:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
            
            #p, p.next, prev = p.next, prev, p
        head1, head2 = head, prev
        print head1.val, head2.val
        while head2:
            if head1.val == head2.val:
                head1 = head1.next
                head2 = head2.next
            else:
                return False
        return True
