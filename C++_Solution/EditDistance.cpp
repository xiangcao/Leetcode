//
//  EditDistance.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/19/15.
//
//

#include <stdio.h>
int minDistance(string word1, string word2) {
    int n1 = word1.size(), n2 = word2.size();
    
    int steps[n1+1][n2+1];
    //fill_n(&steps[n1][n2], n1*n2, INT_MAX);
    for(int i = 0; i <= n1; ++i){
        steps[i][0] = i;
    }
    for(int j = 0; j <= n2; ++j){
        steps[0][j] = j;
    }
    for(int i = 1; i <= n1; ++i){
        for(int j = 1; j <= n2; ++j){
            int replace = steps[i-1][j-1] + (word1[i-1]==word2[j-1]?0:1);
            int minOfDelInsert = min(steps[i-1][j]+1, steps[i][j-1]+1);
            steps[i][j] = min(replace, minOfDelInsert);
            
            /*
             if(word1[i-1] == word2[j-1]){
             steps[i][j] = steps[i-1][j-1];
             }else{
             int mn = min(steps[i-1][j], steps[i][j-1]);
             steps[i][j] = 1 + min(steps[i-1][j-1], mn);
             }*/
        }
    }
    return steps[n1][n2];
}


//one-dimensioN DP
