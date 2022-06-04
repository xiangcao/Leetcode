"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque([root])
        while q[0] != None:
            node = q.popleft()
            q.append(node.left)
            q.append(node.right)
        return all(x == None for x in q)
        //return not any(q)
    
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)

#round 2
    def isCompleteTree(self, root: TreeNode) -> bool:
        que=deque([])
    
        que.append(root)

        while que:

            node=que.popleft()

            if node==None:
                 return not any(que)

            else:

                que.extend( [node.left, node.right] )

        return True
