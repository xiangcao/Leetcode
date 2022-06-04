"""
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

"""

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diags = collections.defaultdict(list)
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols):
                diags[j-i].append(mat[i][j])
        for key in diags:
            diags[key].sort(reverse=True)
            
        for i in range(rows):
            for j in range(cols): 
                mat[i][j] = diags[j-i].pop()
                
        return mat
