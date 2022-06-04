"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        direction = 0
        def cmp(num1, num2):
            if num1 < num2:
                return 1
            if num1 > num2:
                return -1
            return 0
        for i in range(1, len(A)):
            comp =  cmp(A[i], A[i-1])
            if direction == comp:
                continue
            if direction == 0:
                direction = comp
                continue
            if comp == 0:
                continue
            return False
        return True
                
