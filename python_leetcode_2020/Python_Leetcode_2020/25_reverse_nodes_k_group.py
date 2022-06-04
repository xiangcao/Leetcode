"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        count = 0
        current = head
        while count < k and current:
            current = current.next
            count += 1
        if count == k:
            current = self.reverseKGroup(current, k)
            while count > 0:
                tmp = head.next
                head.next = current
                current = head
                head = tmp
                count -= 1
            head = current
        return head
    
    # Iterative
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head
        dummyhead = ListNode(-1)
        dummyhead.next = head
        begin = dummyhead
        i = 0
        while (head):
            i += 1
            if (i%k == 0):
                begin = self.reverse(begin, head.next)
                head = begin.next
            else:
                head = head.next
        return dummyhead.next
    
    # reverse all nodes between begin and end (not including begin and end)
    # returnt the begin node for next k group (i.e., the node before next k nodes) 
    def reverse(self, begin, end):
        curr = begin.next
        prev = begin
        next = None
        first = curr
        while (curr!=end):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        begin.next = prev
        first.next = curr
        return first




# Round 2 (implemented in 20 minutes)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # end is exclusive
        def reverse(start, end):
            prev = None
            while start is not end:
                tmp = start.next
                start.next = prev
                prev = start
                start = tmp
            return prev
        ptr = head        
        prevhead = dummyhead = ListNode(0)
        while ptr:
            start = ptr
            end = ptr
            count = 0
            while end and count < k:
                end = end.next
                count += 1
            if count < k:
                break
            prevhead.next = reverse(start, end)
            start.next = end
            ptr = end
            prevhead = start
        return dummyhead.next
        
            
                
