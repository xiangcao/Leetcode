//
//  DecodeWays.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/19/15.
//
//

#include <stdio.h>

//method 1
int numDecodings(string s) {
    if(s.empty()) return 0 ;
    vector<int> count (s.size(),0);
    for(int i = 0; i < s.size(); ++i){
        for(int j = i; j >= 0; --j){//  if we use "for(int j = i; j >= max(i-1,0); --j){", no need to do line 13
            if(s[j] == '0') continue;
            if(i-j+1 >2) break;
            int num = stoi(s.substr(j,i-j+1));
            if(num <= 26 && num > 0){
                if(j == 0)  count[i] +=1;
                else{
                    if(count[j-1] > 0) count[i] += count[j-1];
                    else continue;
                }
                //count[i] += j>0?count[j-1]:1;
            }
        }
    }
    return count[s.size()-1];
}

//method2

int numDecodings(string s){
    if(s.empty() ||s[0]=='0') return 0;
    
    int prev = 0;
    int cur = 1 ;
    
    //a string with n characters is similar to a stair with n+1 steps
    for(size_t i =1 ;i <= s.size(); ++i){
        if(s[i-1] == '0') cur = 0;
        
        if(i < 2 || !(s[i-2]=='1' || (s[i-2]=='2'&& s[i-2] <= '6'))) prev = 0;
        
        int temp = cur;
        cur = cur + prev;
        prev = temp;
    }
    return cur;
}