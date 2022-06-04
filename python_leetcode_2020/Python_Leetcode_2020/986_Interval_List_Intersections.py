"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

"""
class Solution:
    """
    Intuition

In an interval [a, b], call b the "endpoint".

Among the given intervals, consider the interval A[0] with the smallest endpoint. (Without loss of generality, this interval occurs in array A.)

Then, among the intervals in array B, A[0] can only intersect one such interval in array B. (If two intervals in B intersect A[0], then they both share the endpoint of A[0] -- but intervals in B are disjoint, which is a contradiction.)

Algorithm

If A[0] has the smallest endpoint, it can only intersect B[0]. After, we can discard A[0] since it cannot intersect anything else.

Similarly, if B[0] has the smallest endpoint, it can only intersect A[0], and we can discard B[0] after since it cannot intersect anything else.

We use two pointers, i and j, to virtually manage "discarding" A[0] or B[0] repeatedly.
    """
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aIndex, bIndex = 0, 0
        result=[]
        while (aIndex < len(A) and bIndex < len(B)): 
            maxL = max(A[aIndex][0], B[bIndex][0])
            minR = min(A[aIndex][1], B[bIndex][1])
            if maxL <= minR: 
                result.append([maxL, minR])
            if A[aIndex][1] < B[bIndex][1]:
                aIndex += 1
            elif A[aIndex][1] > B[bIndex][1]:
                bIndex += 1
            else:
                aIndex += 1
                bIndex += 1
                
        return result
            

# 2nd round
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][1]:
                j += 1
            elif A[i][1] < B[j][0]:
                i += 1
            else:
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] > B[j][1]:
                    j += 1
                elif A[i][1] < B[j][1]:
                    i += 1
                else:
                    i += 1
                    j += 1
        return result
                
                
