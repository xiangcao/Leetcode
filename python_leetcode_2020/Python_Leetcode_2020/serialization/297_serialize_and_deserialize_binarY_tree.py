# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                result.append('#')
        result=[]
        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode():
            value = preorderlist.pop()
            # value = next(vals)
            if value == '#':
                return None
            root = TreeNode(value)
            root.left = decode()
            root.right = decode()
            return root
        # vals = iter(data.split(','))
        preorderlist = data.split(',')[::-1]
        return decode()
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
