# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
# another solution http://www.cnblogs.com/lichen782/p/leetcode_Reverse_Nodes_in_kGroup.html 

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #1->2->3->4->5 =>  3->2->1->4->5  <=   5 4 1 2 3
        #the same method used in swapnodesinpair can still apply here with some minor change. but lets try something new
        if not head or k <=1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        head = dummy
        
        while head:
            head = self.reverseNextKNode(head, k)
            print "head val is ", head.val
            print "step " 
        return dummy.next
    def reverseNextKNode(self, head, k):
        """
        :type head: ListNode
        :type k: int
        rtype: ListNode
        """
        p = head
        print " k is ", k
        while p.next and k:
            p = p.next
            k -= 1
            
        if k != 0 :
            return None
        import pdb
        pdb.set_trace() 
        cur = head.next #which is doomed to be the last after reverse
        prev = head
        
        for i in range(k):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head.next.next = cur
        newhead = head.next
        head.next = prev
        raw_input()
        print "head.val is %s, newhead.val is %s" % (head.val, newhead.val)
        return newhead

sol = Solution()
k = 2
head = ListNode(1)
next = ListNode(2)
head.next = next
sol.reverseKGroup(head, k)
