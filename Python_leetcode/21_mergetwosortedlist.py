# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pFinal = lFinal = ListNode(0)
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                pFinal.next = ListNode(p1.val)
                pFinal = pFinal.next
                p1 = p1.next
            else:
                pFinal.next = ListNode(p2.val)
                pFinal = pFinal.next
                p2 = p2.next
        pFinal.next = p1 or p2
        return lFinal.next
        
