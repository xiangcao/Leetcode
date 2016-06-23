"""
 Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combineRecursive(result, curSol, index, k):
            if k == 0:
                result.append(curSol)
                return
            for i in range(index, n+1):
                combineRecursive(result, curSol+[i], i+1, k-1)

        curSol, result = [], []
        combineRecursive(result, curSol, 1, k)
        return result
