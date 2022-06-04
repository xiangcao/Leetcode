"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        overflow = 0
        resultList = ListNode(0)
        resultCopy = resultList
        while l1 is not None and l2 is not None:
            sum = l1.val + l2.val + overflow
            newNode = ListNode(0)
            newNode.val = sum % 10
            resultList.next = newNode
            resultList = resultList.next
            overflow =  sum / 10
            l1 = l1.next
            l2 = l2.next
        remainingL =  l2 if l1 is None else l1
        while remainingL is not None:
            sum = remainingL.val + overflow
            newNode = ListNode(0)
            newNode.val = sum % 10
            resultList.next = newNode
            resultList = resultList.next
            overflow = sum / 10
            remainingL = remainingL.next
        if overflow:
            resultList.next = ListNode(overflow)
        return resultCopy.next

    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next
    
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


# 2nd round
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        carryover = 0
        head = ListNode(-1)
        cur = head
        while node1 or node2:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            carryover, newval = divmod((val1 + val2 + carryover), 10)
            cur.next = ListNode(newval)
            cur = cur.next
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
        if carryover:
            cur.next = ListNode(carryover)
        return head.next
