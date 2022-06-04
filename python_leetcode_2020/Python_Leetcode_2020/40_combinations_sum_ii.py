"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def dfs(idx, target, path):
            if target == 0:
                result.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]: continue
                if candidates[i] <= target:
                    dfs(i+1, target-candidates[i], path+[candidates[i]])
        dfs(0, target, [])
        return result
