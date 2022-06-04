# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # recursive
    def reverseList_1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
    
    # iterative
    def reverseList(self, head: ListNode) -> ListNode:
        preNode, curNode = None, head
        while curNode:
            temp = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = temp
        return preNode
        
