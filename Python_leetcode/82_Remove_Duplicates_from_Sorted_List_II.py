"""
 Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
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
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, dummy.next
        
        while p2 and p2.next:
            while p2.next and p2.next.val == p2.val:
                p2 = p2.next
            if p1.next == p2:
                p1, p2 = p2, p2.next
            else:
                p1.next = p2.next
                p2 = p2.next # I missed this line in my first try. always think about what the pointer will become after each iteration. did it move forward as expected?
                
        return dummy.next
