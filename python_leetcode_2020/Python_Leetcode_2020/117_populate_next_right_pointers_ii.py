"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# testcase [1,2,3,4,5,null,6,7,null,null,null,null,8]
# output   [1,#,2,3,#,4,5,6,#,7, #]
# expected [1,#,2,3,#,4,5,6,#,7,8,#]

#testcase [-9,-3,2,null,4,4,0,-6,null,-5]
#output [-9,#,-3,2,#,4,4,0,#,-6,#]
#expected [-9,#,-3,2,#,4,4,0,#,-6,-5,#]
class Solution:
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost:
            head = leftmost
            leftmost = None
            while head:
                leftmost = leftmost or head.left or head.right

                if head.left:
                    head.left.next = head.right
                if head.next:
                    next_left = head.right or head.left
                    if next_left:
                        while head.next:
                            next_right = head.next.left or head.next.right
                            if next_right:
                                next_left.next = next_right
                                break
                            else:
                                head = head.next
                head = head.next

        return root
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost:
            head = leftmost
            leftmost = None
            prev = None
            while head:
                leftmost = leftmost or head.left or head.right
                if prev:
                    prev.next = head.left or head.right
                if head.left:
                    head.left.next = head.right
                prev = head.right or head.left or prev
                head = head.next
        return root  
    
        
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:    
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
   
    # Iterative;   
    def connect3(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
                
        return root 


# Round 2
# Recursive

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        nextright = root.right or root.left
        if nextright:
            p = root.next
            while p:
                if p.left or p.right:
                    nextright.next = p.left or p.right
                    break
                else:
                    p = p.next
        # Must process right child first
        self.connect(root.right)  
        self.connect(root.left)
        return root
