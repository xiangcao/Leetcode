"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        L, R, T, B = 0, len(matrix[0])-1, 0, len(matrix)-1
        dir = 0
        c = 1
        while L <= R and T <= B:
            if (dir == 0):
                for k in range(L, R+1):
                    matrix[T][k] = c 
                    c += 1
                T += 1
                dir += 1
            elif dir == 1:
                for k in range(T, B+1):
                    matrix[k][R] = c
                    c += 1
                R -= 1
                dir += 1
            elif dir == 2:
                for k in range(R, L-1, -1):
                    matrix[B][k] = c
                    c += 1
                B -= 1
                dir += 1
            else:
                for k in range(B, T-1, -1):
                    matrix[k][L] = c
                    c += 1
                L += 1
                dir = 0
        return matrix

