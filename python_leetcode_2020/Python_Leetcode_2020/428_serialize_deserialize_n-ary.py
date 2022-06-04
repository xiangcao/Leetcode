"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result= []
        def preorder(root):
            if not root:
                return
            size = len(root.children)
            result.append(str(root.val))
            result.append(str(size))
            for c in root.children:
                preorder(c)
        preorder(root)
        return ','.join(result)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        queue = collections.deque(data.split(','))
        def helper():
            root = Node(int(queue.popleft()), [])
            size = int(queue.popleft())
            for i in range(size):
                root.children.append(helper())
            return root
        return helper()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
