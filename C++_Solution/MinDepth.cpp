//
//  MinDepth.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/21/15.
//
/*
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
*/

#include <stdio.h>
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        return dfs(root);
    }
    
    int dfs(TreeNode * root){
        if(!root) return INT_MAX;
        if( !root->left && !root->right){
            return 1;
        }else{
            return min(dfs(root->left), dfs(root->right)) + 1;
        }
    }
};