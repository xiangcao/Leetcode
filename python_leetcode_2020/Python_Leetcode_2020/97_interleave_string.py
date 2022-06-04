"""
Given s1, s2, and s3, find whether s3 is formed by the interleaving of s1 and s2.
"""

class Solution:
    # 2-d DP
    def isInterleave_2d(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s3) != len(s1) + len(s2)):
            return False

        table = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if(i==0 and j==0):
                    table[i][j] = True
                elif i == 0:
                    table[i][j] = (table[i][j-1] and s2[j-1] == s3[i+j-1])
                elif j == 0:
                    table[i][j] = ( table[i-1][j] and s1[i-1] == s3[i+j-1])
                else:
                    table[i][j] = (table[i-1][j] and s1[i-1] == s3[i+j-1] ) or (table[i][j-1] and s2[j-1] == s3[i+j-1] )

        return table[-1][-1]

    # 1-D DP
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s3) != len(s1) + len(s2)):
            return False

        table = [False] * (len(s2)+1)
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if(i==0 and j==0):
                    table[j] = True
                elif i == 0:
                    table[j] = ([j-1] and s2[j-1] == s3[i+j-1])
                elif j == 0:
                    table[j] = ( table[j] and s1[i-1] == s3[i+j-1])
                else:
                    table[j] = (table[j] and s1[i-1] == s3[i+j-1] ) or (table[j-1] and s2[j-1] == s3[i+j-1] )

        return table[-1]
