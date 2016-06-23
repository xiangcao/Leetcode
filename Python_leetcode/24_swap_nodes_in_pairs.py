# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        dummyhead = ListNode(0)
        dummyhead.next = head
        
        curhead = dummyhead
        
        while curhead.next and curhead.next.next:
            n1, n2 = curhead.next, curhead.next.next
            curhead.next, n1.next, n2.next, curhead = n2, n2.next, n1, n1
            
        return dummyhead.next

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1 2 3 4 5 6 -> 2 1 4 3 6 5<- 5 6 3 4 1 2 
        # 1 2 3 -> 2 1 3 <-(3 1 2)
        # 1 2 -> 2 1  <- (1 2)
        dummyhead= ListNode(0)
        dummyhead.next = head
        p1, curhead =  dummyhead, dummyhead
        
        def movetwoforward(node):
            step = 0
            while node.next and step < 2:
                node = node.next
                step += 1
            return node
            
        while True:
            starting = p1
            p1 = movetwoforward(p1)
            if p1 == starting:
                break
            #buggy line. # 1->2->null => 1->2->#->null => 1->2->#->null
            # p1.next, curhead = curhead,  starting.next
            p1.next, curhead, starting.next = curhead,  starting.next, p1.next
            p1 =  starting
        
        #reverse list [curhead->*****->starting]
        
        move = curhead
        moveNext = move.next
        left = None
        # 1 2 3 4 
        while moveNext:
            print move.val
            move.next = left
            move, moveNext, left = moveNext, moveNext.next, move
        
        return left


sol = Solution()
head=ListNode(1)
head.next= ListNode(2)
sol.swapPairs(head)
