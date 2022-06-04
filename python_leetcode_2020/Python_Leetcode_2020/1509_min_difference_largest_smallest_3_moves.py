"""
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

 
"""

class Solution:

    """java
    public int minDifference(int[] A) {
        int n = A.length, res = Integer.MAX_VALUE;
        if (n < 5) return 0;
        Arrays.sort(A);
        for (int i = 0; i < 4; ++i) {
            res = Math.min(res, A[n - 4 + i] - A[i]);
        }
        return res;
    }
    """
    
    def minDifference(self, A):
        A.sort()
        return min(b - a for a, b in zip(A[:4], A[-4:]))
    
    def minDifference(self, A):
        return min(a - b for a,b in zip(heapq.nlargest(4, A), heapq.nsmallest(4, A)[::-1]))
