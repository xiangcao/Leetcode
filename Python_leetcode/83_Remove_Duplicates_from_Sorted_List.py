"""
 Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        p1, p2 = head, head.next
        while p2:
            if p1.val == p2.val:
                p1.next, p2 = p2.next, p2.next
            else:
                p1, p2 = p2, p2.next
        return head
