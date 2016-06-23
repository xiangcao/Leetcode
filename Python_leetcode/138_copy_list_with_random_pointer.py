# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # A->B->C->D
        
        p = head
        while p:
            temp = p.next
            p.next = copy.copy(p)
            p.next.next = temp
            p = temp 
        
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
            
        p = head
        newhead = None
        while p:
            if not newhead:
                newP = newhead = p.next
            else:
                newP.next = p.next
                newP = newP.next
                
            p.next = p.next.next
            p = p.next
            
        return newhead 
            
            
            
# 九张算法
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head == None:
            return None
            
        myMap = {}
        nHead = RandomListNode(head.label)
        myMap[head] = nHead
        p = head
        q = nHead
        while p != None:
            q.random = p.random
            if p.next != None:
                q.next = RandomListNode(p.next.label)
                myMap[p.next] = q.next
            else:
                q.next = None
            p = p.next
            q = q.next
        
        p = nHead
        while p!= None:
            if p.random != None:
                p.random = myMap[p.random]
            p = p.next
        return nHead
