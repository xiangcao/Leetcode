"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        L, R, T, B = 0, len(matrix[0])-1, 0, len(matrix)-1
        dir = 0
        result=[]
        while L <= R and T <= B:
            if (dir == 0):
                for k in range(L, R+1):
                    result.append(matrix[T][k])
                T += 1
                dir += 1
            elif dir == 1:
                for k in range(T, B+1):
                    result.append(matrix[k][R])
                R -= 1
                dir += 1
            elif dir == 2:
                for k in range(R, L-1, -1):
                    result.append(matrix[B][k])
                B -= 1
                dir += 1
            else:
                for k in range(B, T-1, -1):
                    result.append(matrix[k][L])
                L += 1
                dir = 0
        return result
                
        
