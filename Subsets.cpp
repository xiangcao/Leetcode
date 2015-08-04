//
//  Subsets.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/19/15.
//
//
//subsets I
/*
 Given a set of distinct integers, nums, return all possible subsets.
 
 Note:
 
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
 
 For example,
 If nums = [1,2,3], a solution is:
 
 [
 [3],
 [1],
 [2],
 [1,2,3],
 [1,3],
 [2,3],
 [1,2],
 []
 ]


*/

#include <stdio.h>

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        result.push_back({});
        for(int i=0; i<nums.size(); ++i){
            //for(vector<int> elem: result){
            int n = result.size();
            for(int j =0; j< n; ++j){ //for(int j =0; j< result.size(); ++j){
                vector<int> elem(result[j].begin(), result[j].end());
                result.push_back(elem);
            }
            n = result.size();
            for(int j = result.size()/2; j < n; ++j){ //j < result.size();
                result[j].push_back(nums[i]);
            }
        }
        return result;
    }
};


/*
 
 Subsets II
 
*/