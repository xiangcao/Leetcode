"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.
"""
class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(A[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                A[i][j] = d[i - j].pop()
        return A
