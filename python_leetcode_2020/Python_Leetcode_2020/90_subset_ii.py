"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        def dfs(subset, cur_index, last_added):
            if cur_index == len(nums):
                return result.append(subset)
            dfs(subset, cur_index+1, False)
            if cur_index > 0 and nums[cur_index] == nums[cur_index-1] and not last_added:
                    return
            dfs(subset+[nums[cur_index]], cur_index+1, True)

        dfs([], 0, False)
        return result     
