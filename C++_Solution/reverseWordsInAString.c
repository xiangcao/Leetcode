//
//  reverseWordsInAString.c
//  Leetcode
//
//  Created by Xiangcao Liu on 7/27/15.
//
//
/*
 
 Reverse Words in a String
 Total Accepted: 67 Total Submissions: 412My Submissions
 
 Given an input string, reverse the string word by word.
 
 For example,
 Given s = "the sky is blue",
 return "blue is sky the".
 
 click to show clarification.
 Clarification:
 
 What constitutes a word?
 A sequence of non-space characters constitutes a word.
 Could the input string contain leading or trailing spaces?
 Yes. However, your reversed string should not contain leading or trailing spaces.
 How about multiple spaces between two words?
 Reduce them to a single space in the reversed string.
 

 
 
*/
#include <stdio.h>

//O(1) space, O(N) time
void reverseWords(char *s) {
    int index = 0 ;
    int length = strlen(s);
    bool singleSpace = true;
    bool leadingSpace = true;
    
    // Input: " 1"    Output: "1 "    Expected: "1"
    // Input: "1 "    Output: " 1"    Expected: "1"
    //remove space
    for(int i = 0; i < length; ++i){
        if(s[i] != ' '){
            if(i > 0 && s[i-1]==' ' && !leadingSpace) s[index++] = s[i-1];
            s[index++] = s[i];
            singleSpace = false;
            leadingSpace = false;
        }else{
            if(singleSpace) continue;
            else singleSpace = true;
            //s[index++] = s[i];
        }
    }
    s[index] = '\0';
    
    //reverse each word letter by letter
    int begin = -1, end = -1;
    
    //Input: "hi!" Output: "!ih" Expected: "hi!"
    
    for(index = 0; index <= strlen(s); ++index){
        if(s[index] == ' '||s[index] == '\0'){
            if(begin >= 0 && end == -1){
                end = index-1;
                reverseSingleWord(s, begin, end);
                begin = -1;
                end = -1;
            }
            else continue;
        }
        if(s[index] != ' '){
            if(begin ==-1){
                begin = index;
            }else{
                continue;
            }
        }
    }
    
    //reverse the whole string letter by letter
    reverseSingleWord(s, 0, strlen(s)-1);
    
}

void reverseSingleWord(char *s, int begin, int end){
    while(begin < end){
        char temp = s[begin];
        s[begin] = s[end];
        s[end] = temp;
        ++begin;
        --end;
    }
}