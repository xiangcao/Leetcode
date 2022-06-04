# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstElement, secondElement = None, None
        # The reason for this initialization is to avoid null pointer exception in the first comparison when prevElement has not been initialized
        prevElement = TreeNode(float('-inf'))
        def traverse(root):
            nonlocal firstElement,secondElement,prevElement
            if (root == None):
                return
            traverse(root.left)
        
            # If first element has not been found, assign it to prevElement (refer to 6 in the example above)
            if (firstElement == None and prevElement.val >= root.val):
                firstElement = prevElement

            #If first element is found, assign the second element to the root (refer to 2 in the example above)
            if (firstElement != None and prevElement.val >= root.val):
                secondElement = root     
            prevElement = root

            traverse(root.right)
       
        # In order traversal to find the two elements
        traverse(root)

        # Swap the values of the two nodes
        temp = firstElement.val
        firstElement.val = secondElement.val
        secondElement.val = temp


# https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
# https://leetcode.com/problems/recover-binary-search-tree/discuss/32559/Detail-Explain-about-How-Morris-Traversal-Finds-two-Incorrect-Pointer

# Morris In-order; space O(1)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # predecessor is a Morris predecessor. 
        # In the 'loop' cases it could be equal to the node itself predecessor == root.
        # pred is a 'true' predecessor, 
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None
        
        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:       
                # Predecessor node is one step left 
                # and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
 
                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred 
                    pred = root
                    
                    predecessor.right = None
                    root = root.right
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred 
                pred = root
                
                root = root.right
        
        x.val, y.val = y.val, x.val
