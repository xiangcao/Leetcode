# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level order: https://leetcode.com/discuss/73461/short-and-straight-forward-bfs-java-code-with-a-queue
# pre-order https://leetcode.com/discuss/66117/easy-to-understand-java-solution
# pre-order https://leetcode.com/discuss/66147/recursive-preorder-python-and-c-o-n 

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        if not root:
            return result
        # Level Order
        queue=collections.deque([root])
        while queue:
            root = queue.pop()
            result.append("#")
            if root:
                result.append(str(root.val))
                queue.appendleft(root.left)
                queue.appendleft(root.right)
        return "".join(result[1:])       


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        index = 0
        if not data:
            return None
        data = data.split("#")
        newRoot = TreeNode(data[0])
        queue=collections.deque([newRoot]) 
        index = 1 
        while index < len(data):
            curNode = queue.pop()
            if data[index]:
                curNode.left = TreeNode(data[index])
                queue.appendleft(curNode.left)
            index += 1
            if data[index]:
                curNode.right = TreeNode(data[index])
                queue.appendleft(curNode.right)
            index += 1
        return newRoot
        
       

#Preorder
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        if not root:
            return result
        # Level Order
        queue=collections.deque([root])
        while queue:
            root = queue.pop()
            if root:
                result.append(str(root.val))
                queue.appendleft(root.left)
                queue.appendleft(root.right)
            else:
                result.append("#")
        return " ".join(result)       


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(" ")
        
        newRoot = TreeNode(data[0])
        queue=collections.deque([newRoot]) 
        index = 1 
        while index < len(data):
            curNode = queue.pop()
            if data[index] != "#":
                curNode.left = TreeNode(data[index])
                queue.appendleft(curNode.left)
            index += 1
            if index < len(data) and data[index] != "#":
                curNode.right = TreeNode(data[index])
                queue.appendleft(curNode.right)
            index += 1
        return newRoot
