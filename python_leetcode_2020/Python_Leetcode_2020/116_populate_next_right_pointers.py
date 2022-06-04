"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

class Solution:
    #BFS
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue=collections.deque([])
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size-1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
    
    # Iteration without extra space (O(1) space)
    def connect(self, root: 'Node') -> 'Node':
        p = root
        while p:
            left = p.left
            q = p
            while q:
                if q.left:
                    q.left.next = q.right
                if q.next and q.right:
                    q.right.next = q.next.left
                q = q.next
            p = left
        return root
        
    # answer on leetcode: better code than above   
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        
        return root  

# round 2
# recursive approach
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        if root.right:
            if root.next:
                root.right.next = root.next.left or root.next.right
        self.connect(root.left)
        self.connect(root.right)
        return root
