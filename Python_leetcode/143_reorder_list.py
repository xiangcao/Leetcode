# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #accepted
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #1 find the middle point. 
        #2 Reverse: reverse the nodes after the middle point. if even # of nodes, the middle point is the left one. 
        #3 Merge: insert each of the node after middle point into the nodes before middle point.
        
        if not head or not head.next:
            return
        slow, quick = head, head.next
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        #slow is the middle point
        p = slow.next
        prev = None
        while p:
            p.next, p, prev = prev, p.next, p
        slow.next = prev # this is the evil. simply changing this to slow.next = None, will avoid all the hassle below
        
        l1, l2 = head, slow.next
        
        
        while l1 and l2:
            temp = l1.next
            #l1.next, l2, slow.next  = l2, l2.next,l2.next
            l1.next = l2
            l2 = l2.next
            if slow != l1: #to fix the [1,2], [1,2,3,4],etc
                slow.next =l2
            if l1.next != temp: #to fix the case [1,2], [1,2,3,4], etc
                l1.next.next = temp
            l1 = temp 
    
    def printList(self, head):
        while head:
            print head.val
            head = head.next

    #accepted
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #1 find the middle point. 
        #2 Reverse: reverse the nodes after the middle point. if even # of nodes, the middle point is the left one. 
        #3 Merge: insert each of the node after middle point into the nodes before middle point.
        
        if not head or not head.next or not head.next.next:
            return
        slow, quick = head, head.next
        while quick and quick.next:
            slow = slow.next
            quick = quick.next.next
        #slow is the middle point
        p = slow.next
        prev = None
        while p:
            p.next, p, prev = prev, p.next, p
            
        l1, l2 = head, prev
        slow.next = None
        
        while l1 and l2:
            temp = l1.next
            l1.next, l = l2, l2.next
            l1.next.next = temp
            l1 = temp 



sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
#head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
sol.reorderList(head)
sol.printList(head)
