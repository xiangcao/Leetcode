https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.order = 0 
        self.result = None
        def inorder(root):
            if not root:
                return False
            if inorder(root.left):
                return True
            self.order += 1
            if self.order == k:
                self.result = root
                return True
            if inorder(root.right):
                return True
            
        inorder(root)
        return self.result.val

     def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

Follow up
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Insert and delete in a BST were discussed last week, the time complexity of these operations is \mathcal{O}(H)O(H), where HH is a height of binary tree, and H = \log NH=logN for the balanced tree.

Hence without any optimisation insert/delete + search of kth element has \mathcal{O}(2H + k)O(2H+k) complexity. How to optimise that?

That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :

Insert

Delete

Find kth smallest

Seems like a database description, isn't it? Let's use here the same logic as for LRU cache design, and combine an indexing structure (we could keep BST here) with a double linked list.

Such a structure would provide:

O(H) time for the insert and delete.

O(k) for the search of kth smallest.


The overall time complexity for insert/delete + search of kth smallest is \mathcal{O}(H + k)O(H+k) instead of \mathcal{O}(2H + k)O(2H+k).

Complexity Analysis

Time complexity for insert/delete + search of kth smallest: O(H+k), where H is a tree height. O(logN+k) in the average case, O(N+k) in the worst case.

Space complexity : \mathcal{O}(N)O(N) to keep the linked list.
