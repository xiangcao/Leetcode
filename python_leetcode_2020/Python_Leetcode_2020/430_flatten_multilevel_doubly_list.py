"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# essentially it is the same problem of '114 Flatten Binary Tree to Linked List'
# only difference is here we need to convert to a double linkedin list
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        #return the tail after flatten all nodes under root
        def flatten(root):
            if not root:
                return None
            childtail = flatten(root.child)
            nexttail = flatten(root.next)
            if childtail:
                childtail.next = root.next
                if root.next:
                    root.next.prev = childtail
                root.next = root.child
                root.child.prev = root
                root.child = None
            return nexttail or childtail or root
        flatten(head)
        return head
