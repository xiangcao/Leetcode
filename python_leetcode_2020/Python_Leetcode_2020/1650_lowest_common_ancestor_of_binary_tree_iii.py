"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
"""
The idea is fairly simple (and the same as finding the convergence point of 2 linked lists). We keep two pointers, p1 and p2. Originally, these pointers point to q and p, respectively. Then we follow their parent pointers until they point to the same node. When either of the pointers points to root, we set it to the other original starting node. For example, when p1 points to root (i.e p1.parent is None), assign q to p1.
"""
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1
