"""
 Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false. 
"""

#https://leetcode.com/discuss/86593/clean-and-short-with-comments-c
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        
        min = float("inf")
        secondMin = float("inf")
        
        for i in nums:
            if i <= min:
                min = i
            elif i <= secondMin:
                secondMin = i
            else:
                return True
        return False
