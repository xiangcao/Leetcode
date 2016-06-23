"""
 Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 1
        end = len(nums)-1
        
        # find the first number larger or equal to the duplicate number
        while begin < end:
            mid = begin + (end - begin) / 2 
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                begin = mid + 1
            else:
                end = mid
        return begin
                
        
#http://www.cnblogs.com/grandyang/p/4843654.html 
