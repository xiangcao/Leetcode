# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #iterative
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while (pre.next != None):
            if (pre.next.val == val):
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
    
    #recursive
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

