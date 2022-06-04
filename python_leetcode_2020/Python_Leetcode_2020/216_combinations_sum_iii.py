"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def dfs(idx, target, path):
            if target == 0 and len(path) == k:
                result.append(path)
                return
            if target == 0 or len(path) == k:
                return
            for i in range(idx, 10):
                if i <= target:
                    dfs(i+1, target-i, path+[i])
        dfs(1, n, [])
        return result
