"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while(l1 ):
            s1.append(l1.val)
            l1 = l1.next
        while(l2):
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        result = ListNode(0)
        while (s1 or s2):
            if (s1): carry += s1.pop()
            if (s2): carry += s2.pop()
            result.val = carry % 10
            head = ListNode(carry / 10)
            head.next = result
            result = head
            carry /= 10
        
        return result.next if result.val == 0 else result
