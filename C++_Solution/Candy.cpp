//
//  Candy.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/18/15.
//
//

#include <stdio.h>
class Solution {
public:
    //Note: nothings says about if two neighbor has equal rating, should they equal number of candies or not.
    //Input: [1,2,2]  Output: 5  Expected: 4
    
    int candy(vector<int>& ratings) {
        vector<int> candy(ratings.size());
        candy[0] = 1;
        for(int i = 1; i < ratings.size(); ++i){
            if(ratings[i] > ratings[i-1]){
                candy[i] = candy[i-1] + 1;
            }else if(ratings[i] <= ratings[i-1]){
                candy[i] = 1 ;
            }/*else{
              candy[i] = candy[i-1];
              }*/
        }
        for(int i = ratings.size()-2; i >= 0; --i){
            if(ratings[i]>ratings[i+1]){
                if(candy[i] <= candy[i+1]){
                    candy[i] = candy[i+1] + 1;
                }
            }
            /*else{
             if(ratings[i] == ratings[i+1] && candy[i] < candy[i+1]) candy[i] = candy[i+1];
             }*/
        }
        int total = 0 ;
        for(int i = 0; i < candy.size(); ++i){
            total += candy[i];
        }
        return total;
    }
};