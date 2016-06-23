# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    
    # Accepted 
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        table = {}
        def cloneGraphHelper(node, table):
            if not node:
                return None
            
            if node.label in table:
                return table[node.label]
            copy = UndirectedGraphNode(node.label)
            table[node.label] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(cloneGraphHelper(neighbor,table))
                
            return copy
        return cloneGraphHelper(node, table)
