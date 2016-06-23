//
//  alien-language-dictionary-problem.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 8/2/15.
//
//

#include <stdio.h>


#include<stack>
#include<iostream>
using namespace std;
//http://massivealgorithms.blogspot.com/2014/07/given-sorted-dictionary-of-alien.html
//https://theetaone.wordpress.com/2014/08/17/alien-language-dictionary-problem/

class Graph{
    int V;  //no of vertices;
    
    //Pointer to array of adjency lists
    list<int> * adj;
    
    //A function used by Topological sort
    void topologicalSortUtil(int v, bool visited[], stack<int> & Stack){
        if(visited[v]) return;
        list<int> iterator it;
        visited[v] = true;
        for(it = adj[v].begin(); it != adj[v].end(); ++it){
            if( !visited[*it] ){
                topologicalSortUtil(*it, visited, Stack);
            }
        }
        Stack.push_back(v);
    }
public:
    Graph(int V){
        this->V = V;
        adj = new list<int>[V];
    }
    
    void addEdge(int v, int w){
        adj[v].push_back(w);
    }
    void topologicalSort();
    
    
    
};

void Graph::topologicalSort(){
    stack<int> Stack;
    //Mark all the vertices as not visited
    bool * visited = new bool[V];
    for(int i = 0; i < V; ++i){
        visited[i] = false;
    }
    for(int i = 0;  i < V; ++i){
        if(!visited[i]){
            topologicalSortUtil(i, visited, Stack);
        }
    }
    while(!Stack.empty()){
        cout<< char (Stack.top() + 'a') <<endl;
        Stack.pop();
    }
}

void printOrder(string words[], int n, int alpha){
    //create a graph with "alpha" number of nodes
    Graph g(alpha);
    
    //Process all adjacent pair of words and find the first mismatching
    for(int i = 0 ; i < n-1; ++i){
        string word1 = words[i], word2 = words[i+1];
        for(int j = 0; j < min(word1.length(), word2.length()); ++j){
            if(word1[j] != word2[j]){
                g.addEdge(word1[j]-'a', word2[j]-'a');
                break;
            }
        }
    }
    
    g.topologicalSort();
}