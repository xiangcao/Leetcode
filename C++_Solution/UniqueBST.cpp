//
//  UniqueBST.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/21/15.
//https://leetcode.com/problems/unique-binary-search-trees/
//

#include <stdio.h>
//unique BST I:  Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

class Solution {
public:
    int numTrees(int n) {
        if(n == 1 || n == 0) return 1;
        vector<int> num(n+1, 1);
        for(int k = 1; k <= n; ++k){
            int sum = 0;
            for(int i = 0; i < k; ++i){
                sum += num[i] * num[k-i-1];
            }
            num[k] = sum;
        }
        return num[n];
    }
    
    //Recursion timelimit exceeded
    int numTreesR(int n) {
        if(n == 1 || n == 0) return 1;
        int sum = 0;
        for(int i = 0; i < n; ++i){
            sum += numTreesR(i) * numTreesR(n-i-1);
        }
        return sum;
    }
    //5: 4, 3,2*2, 3, 4,
};


//Unique BST II Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
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
    vector<TreeNode*> generateTrees(int n) {
        return generateTrees(1, n);
    }
    vector<TreeNode*> generateTrees(int left, int right) {
        vector<TreeNode *> result;
        if(left > right) {
            result.push_back(nullptr);
            return result;
        }
        for(int root = left; root <= right; ++root){
            vector<TreeNode *> leftSubTrees = generateTrees(left, root-1);
            vector<TreeNode *> rightSubTrees = generateTrees(root+1, right);
            for(auto elemL: leftSubTrees){
                for(auto elemR: rightSubTrees){
                    TreeNode * parent = new TreeNode(root);
                    parent->left = elemL;
                    parent->right = elemR;
                    result.push_back(parent);
                }
            }
        }
        return result;
    }
    
};