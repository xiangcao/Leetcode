"""
Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.
"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution(object):
    # Idea: Three cases:
    # Case 1). The value of new node sits between the minimal and maximal values of the current list. As a result, it should be inserted within the list.
    # Case 2). The value of new node goes beyond the minimal and maximal values of the current list, either less than the minimal value or greater than the maximal value. In either case, the new node should be added right after the tail node (i.e. the node with the maximal value of the list).
    # Case 3). Finally, there is one case that does not fall into any of the above two cases. This is the case where the list contains uniform values.
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev, cur = head, head.next
        while True:
            if prev.val <= insertVal <= cur.val:
                break
            if prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    break
            prev, cur = cur, cur.next
            if prev == head:
                break

        prev.next = Node(insertVal, cur)
        return head
        
