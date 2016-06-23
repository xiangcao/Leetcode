"""
 Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

    Expected runtime complexity is in O(log n) and the input is sorted.

"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        left, right = 0, len(citations)-1
        while left<right:
            mid = left + (right-left)/2
            if citations[mid] >= (len(citations)-mid):
                right = mid
            else:
                left = mid + 1
        #left is candidate
        if citations[left] >= (len(citations)- left):
            return len(citations)- left
        else:
            return 0
        
        
