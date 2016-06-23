//
//  WordSearchII.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 8/3/15.
//
//

/*
 Given a 2D board and a list of words from the dictionary, find all words in the board.
 
 Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
 
 For example,
 Given words = ["oath","pea","eat","rain"] and board =
 
 [
 ['o','a','a','n'],
 ['e','t','a','e'],
 ['i','h','k','r'],
 ['i','f','l','v']
 ]
 
 Return ["eat","oath"].
 
 Note:
 You may assume that all inputs are consist of lowercase letters a-z.
 
 click to show hint.
 
 You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
 
 If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
 */

//

#ifndef __Leetcode__WordSearchII__
#define __Leetcode__WordSearchII__

#include <stdio.h>

#endif /* defined(__Leetcode__WordSearchII__) */

class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode():children(26,nullptr), val(0) {
    }
    int val;
    vector<TrieNode * > children;
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

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie trie;
        for(string & word: words){
            trie.insert(word);
        }
        int m = board.size();
        int n = board[0].size();
        vector<deque<bool>> visited(m, deque<bool>(n, false));
        vector<string> result;
        string word="";
        for(int i  = 0 ; i < m ; ++i){
            for(int j = 0 ; j  < n ; ++j){
                dfs(board, i, j, trie, word, visited, result);
            }
        }
        
        sort(result.begin(), result.end());
        result.erase(unique(result.begin(), result.end()), result.end());
        return result;
        
    }
    
    void dfs(vector<vector<char>>& board, int i, int j, Trie & trie, string constructedWord,
             vector<deque<bool>> & visited, vector<string> & result){
        if(i>=board.size() || j >= board[0].size() || i <0 || j<0) return;
        if(visited[i][j]) return;
        constructedWord.push_back(board[i][j]);
        if(!trie.startsWith(constructedWord)){
            return;
        }
        if(trie.search(constructedWord)) {
            result.push_back(constructedWord);
            //return;
        }
        
        visited[i][j] = true;
        dfs(board, i-1, j, trie, constructedWord, visited, result);
        dfs(board, i+1, j, trie, constructedWord, visited, result);
        dfs(board, i, j+1, trie, constructedWord, visited, result);
        dfs(board, i, j-1, trie, constructedWord, visited, result);
        visited[i][j] = false;
        //  constructedWord.pop_back();
    }
};
