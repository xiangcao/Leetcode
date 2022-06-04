"""
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
"""

class Solution:
    def pathInZigZagTree(self, label):
        res = [] # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count*2: # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0: # O(log n) time
            res.append(label)
            level_max = 2**(level) - 1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        return res[::-1] # O(n) time
