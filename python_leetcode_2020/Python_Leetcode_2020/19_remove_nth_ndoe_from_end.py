"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Iterative solution
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1, head)
        first = second = dummy
        for i in range(n+1):
            first = first.next
        while first and second:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    # Recursive solution
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def dfs(node):
            if not node:
                return 0
            reverse = dfs(node.next)
            if reverse == n:
                node.next = node.next.next
            return reverse + 1
        reverse = dfs(head)
        return head if reverse > n else head.next
