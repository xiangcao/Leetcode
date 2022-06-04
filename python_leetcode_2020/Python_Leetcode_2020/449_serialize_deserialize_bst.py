"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # preorder iterative traversal
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        result = []
        stack=[root]
        while stack:
            node = stack.pop()
            result.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return "#".join(result)

    # Keep poping when building tree node 
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        elements = collections.deque([int(i) for i in data.split("#")])
        def helper(low, high):
            if not elements or elements[0] < low or elements[0] > high:
                return None

            newnode = TreeNode(int(elements.popleft()))

            newnode.left = helper(low, newnode.val)
            newnode.right = helper(newnode.val, high)
            return newnode
        return helper(float("-inf"), float("inf"))

    # find the first node that's larger than root, which will be the right tree
    def deserialize2(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        elements = data.split("#")
        def helper(left, right):
            if left > right:
                return None

            newnode = TreeNode(int(elements[left]))
            if left == right:
                return newnode

            rightchild = left + 1
            while rightchild <= right:
                if int(elements[rightchild]) < int(newnode.val):
                    rightchild += 1
                else:
                    break
            newnode.left = helper(left+1, rightchild-1)
            newnode.right = helper(rightchild, right)
            return newnode
        return helper(0, len(elements)-1)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
