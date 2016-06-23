# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p1,p2 = head, head
        head2 = ListNode(0)
        prevP1, head2.next = head2, head
        #head2.next = head
        #prevP1 = head2
        for i in range(n-1):
            if not p2:
                break
            p2 = p2.next
        if p2 is None:
            return head

        while p2.next:
            prevP1 = p1 
            p1 = p1.next
            p2 = p2.next
    
        prevP1.next = p1.next
        return head2.next
            
      
     def removeNthFromEnd(self, head, n):
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:
            p1=p1.next; p2=p2.next
        p2.next=p2.next.next
        return dummy.next

