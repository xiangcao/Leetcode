//
//  Trie.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/18/15.
//
//
/*
 mplement a trie with insert, search, and startsWith methods.
 
 Note:
 You may assume that all inputs are consist of lowercase letters a-z.
 
 */
#include <stdio.h>
class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode():children(26,nullptr), val(0) {
    }
    int val; //if val is 1, it means this node is a leaf node
    vector<TrieNode * > children;
};


class TrieNode{
public:
    TrieNode():children(26, nullptr), val(0){
        
    }
    int val;
    vector<TrieNode*> children;
};

class Trie{
public:
    Trie(){
        root = new TrieNode();
    }
    void insert(string word){
        TrieNode * p = root;
        for(char & c: word){
            if(!p->children[c-'a']){
                p->children[c-'a'] = new TrieNode();
            }
            p = p->children[c-'a'];
        }
        p->val = 1 ;
    }
    void startWith(string prefix){
        TrieNode * p = root;
        for(char & c: prefix){
            if(!p->children[c-'a']){
                return false;
            }
            p = p->children[c-'a'];
        }
        return true;
    }
    
private:
    TrieNode * root;
};
class Trie {
public:
    Trie() {
        root = new TrieNode();
    }
    
    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode * p = root;
        for(char & c: word){
            if(!p->children[c-'a']){
                p->children[c-'a'] = new TrieNode();
            }
            p = p->children[c-'a'];
        }
        p->val = 1;
    }
    
    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode * p = root;
        for(char & c: word){
            if(!p->children[c-'a']){
                return false;
            }
            p = p->children[c-'a'];
        }
        if(p->val) return true;
        else return false;
    }
    
    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode * p = root;
        for(char & c: prefix){
            if(!p->children[c-'a']){
                return false;
            }
            p = p->children[c-'a'];
        }
        return true;
    }
    
private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");