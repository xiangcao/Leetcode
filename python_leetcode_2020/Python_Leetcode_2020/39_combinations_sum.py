"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def dfs(idx, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(idx, len(candidates)):
                if candidates[i] <= target:
                    dfs(i, target-candidates[i], path+[candidates[i]])
        dfs(0, target, [])
        return result
