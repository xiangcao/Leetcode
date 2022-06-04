"""
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.


The mentioned steps are done level by level, it is guaranteed that every node in the given tree has either 0 or 2 children.

Constraints:

The number of nodes in the tree will be in the range [0, 10].
1 <= Node.val <= 10
Every node has either 0 or 2 children.


"""

Recursive solutino
TreeNode* upsideDownBinaryTree(TreeNode* root) {
    if (!root || !root->left) return root;
    TreeNode* cur_left = root->left;
    TreeNode* cur_right = root->right;
    TreeNode* new_root = upsideDownBinaryTree(root->left);
    cur_left->right = root;
    cur_left->left = cur_right;
    root->left = nullptr;
    root->right = nullptr;
    return new_root;
}


Java recursive
This is not a very intuitive problem for me, I have to spent quite a while drawing figures to understand it. As shown in the figure, 1 shows the original tree, you can think about it as a comb, with 1, 2, 4 form the bone, and 3, 5 as the teeth. All we need to do is flip the teeth direction as shown in figure 2. We will remove the link 1--3, 2--5, and add link 2--3, and 4--5. And node 4 will be the new root.

As the recursive solution, we will keep recurse on the left child and once we are are done, we found the newRoot, which is 4 for this case. At this point, we will need to set the new children for node 2, basically the new left node is 3, and right node is 1. Here is the recursive solution:

public TreeNode upsideDownBinaryTree(TreeNode root) {
    if(root == null || root.left == null) {
        return root;
    }
    
    TreeNode newRoot = upsideDownBinaryTree(root.left);
    root.left.left = root.right;   // node 2 left children
    root.left.right = root;         // node 2 right children
    root.left = null;
    root.right = null;
    return newRoot;
}

# iterative
public TreeNode upsideDownBinaryTree(TreeNode root) {
    TreeNode curr = root;
    TreeNode next = null;
    TreeNode temp = null;
    TreeNode prev = null;
    
    while(curr != null) {
        next = curr.left;
        
        // swapping nodes now, need temp to keep the previous right child
        curr.left = temp;
        temp = curr.right;
        curr.right = prev;
        
        prev = curr;
        curr = next;
    }
    return prev;
}  
