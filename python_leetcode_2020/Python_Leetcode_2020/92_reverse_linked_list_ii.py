"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return None
        dummy = ListNode(0) # create a dummy node to mark the head of this list
        dummy.next = head
        pre = dummy # make a pointer pre as a marker for the node before reversing
        for i in range(m-1): pre = pre.next
        start = pre.next # a pointer to the beginning of a sub-list that will be reversed
        then = start.next # a pointer to a node that will be reversed

        # 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3
        # dummy-> 1 -> 2 -> 3 -> 4 -> 5
        for i in range(n-m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        # first reversing : dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
        # second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5 (finish)
        return dummy.nexti
