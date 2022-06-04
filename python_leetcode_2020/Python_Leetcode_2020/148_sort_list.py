"""
Sort a linked list in O(n log n) time using constant space complexity.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # recursion
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #[4,2]
        if (head == None or head.next == None):
            return head

        # step 1. cut the list to two halves
        slow = head
        fast = head
        prev = None
        # second child list must start with slow pointer; 
        # this is because if there is only two elements in the list, slow point to the second element; 
        # to reduce the child list size, we have to split it before the slower pointer, otherwise we will get stuck with the same size and infinite loop
        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # step 2. sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        def merge(l1, l2):
            l = ListNode(0)
            p = l

            while (l1 != None and l2 != None):
                if (l1.val < l2.val):
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next

            if (l1 != None):
                p.next = l1

            if (l2 != None):
                p.next = l2

            return l.next
        
        # step 3. merge l1 and l2
        return merge(l1, l2)
