//
//  Minimum_Path_Sum.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/17/15.
//
//

#include "Minimum_Path_Sum.h"
#include<vector>
#include<math>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int n = grid.size();
        if(n == 0) return 0;
        int m = grid[0].size();
        vector<int> distance(m);
        distance[0] = grid[0][0];
        
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(i ==0 && j==0){
                    continue;
                }
                distance[j] = min( j>0?distance[j-1]:INT_MAX, i>0?distance[j]:INT_MAX ) + grid[i][j] ;
            }
        }
        
        return distance[m-1];
        
    }
};