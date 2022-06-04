# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        if not (root.left or root.right):
            return [root.val]
        left_boundary = [root.val]
        node = root.left
        while node:
            if node.left or node.right:
                left_boundary.append(node.val)

            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                break

        def addLeaves(node):
            if node.left:
                addLeaves(node.left)
            if node.right:
                addLeaves(node.right)
            if not (node.left or node.right):
                left_boundary.append(node.val)
            
        addLeaves(root)
        right_boundary=[]
        node = root.right
        while node:
            if (node.right or node.left):
                right_boundary.append(node.val)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                break
        left_boundary += right_boundary[::-1]
        return left_boundary
# test case: [1]
# test case3: [3,2,null,null,4,1]

                
