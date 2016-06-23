//
//  Subsets II.cpp
//  Leetcode
//
//  Created by Xiangcao Liu on 7/19/15.
//
//
/*
 Given a collection of integers that might contain duplicates, nums, return all possible subsets.
 
 Note:
 
 Elements in a subset must be in non-descending order.
 The solution set must not contain duplicate subsets.
 
 For example,
 If nums = [1,2,2], a solution is:
 
 [
 [2],
 [1],
 [1,2,2],
 [2,2],
 [1,2],
 []
 ]

 */

#include <stdio.h>


class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        vector<int> path;
        subsetsWithDup(nums, result, path, 0, INT_MIN);
        return result;
    }
    void subsetsWithDup(vector<int> & nums, vector<vector<int>> &result, vector<int> & path, int curIndex, int prev){
        if(curIndex == nums.size()){
            result.push_back(path);
            return;
        }
        if(curIndex == 0 || (nums[curIndex] != prev)){
            subsetsWithDup(nums, result, path, curIndex+1, prev);
        }
        path.push_back(nums[curIndex]);
        prev = nums[curIndex];
        subsetsWithDup(nums, result, path, curIndex+1, prev);
        path.pop_back();
    }
};