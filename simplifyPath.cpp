//
//  simplifyPath.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/27/15.
//
//

/*
 
 Given an absolute path for a file (Unix-style), simplify it.
 
 For example,
 path = "/home/", => "/home"
 path = "/a/./b/../../c/", => "/c"
 
 Corner Cases:
 
 Did you consider the case where path = "/../"?
 In this case, you should return "/".
 Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
 In this case, you should ignore redundant slashes and return "/home/foo".

 */
#include <stdio.h>


class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stack;
        int i = 0 ;
        while(i<path.length()){
            while(path[i]=='/' && i <path.length()) ++i;
            if(i == path.length()) break;
            int start = i ;
            while(path[i] != '/' && i < path.length()) ++i;
            int end = i - 1 ;
            string elem = path.substr(start, end-start+1);
            if(elem ==".."){
                if(!stack.empty())
                    stack.pop_back();
            }else if(elem!="."){
                stack.push_back(elem);
            }
        }
        string result ;
        if(stack.empty()) return "/";
        for(int i  = 0 ; i < stack.size(); ++i){
            result += "/"+ stack[i];
        }
        return result ;
    }
    /*
     Input: "/."
     Output: "/."
     Expected: "/"
     string simplifyPath(string path) {
     string result ;
     char prev =' ';
     bool newSegment = false;
     int i = 0 ;
     for(; i<path.length(); ++i){
     if(path[i]== ' ') continue;
     else break;
     }
     for(; i<path.length(); ++i){
     if(path[i] == '/'){
     if(prev == '/' ) continue;
     if(prev == '.'){
     result.pop_back();
     prev = '/';
     continue;
     }
     result.push_back(path[i]);
     prev = '/';
     newSegment = true;
     }else if(path[i] == '.'){
     if(prev == '.' && newSegment){
     if((i+1)<path.length() && path[i+1] == '.'){
     result.push_back('.');//result.push_back(path[i]);
     result.push_back('.');//result.push_back(path[i+1]);
     ++i;
     continue;
     }
     result.pop_back();
     result.pop_back();
     while(result.back() !='/'&& result.length()>0){
     result.pop_back();
     }
     if(result.length()==0) prev =' ';
     else prev = '/';
     continue;
     }else{
     result.push_back(path[i]);
     prev = '.';
     }
     }else{
     result.push_back(path[i]);
     prev = path[i];
     newSegment = false;
     }
     }
     return result;
     }*/
};