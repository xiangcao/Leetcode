class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return  ( 1 + n ) * n /2 - sum(nums)
       
#http://www.cnblogs.com/grandyang/p/4756677.html  3 different solution 
