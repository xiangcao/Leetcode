class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))

#219
#Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k. 
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i - dict[v] <= k:
                return True
            dict[v] = i
        return False
        
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        for i, v in enumerate(nums):
            if i > k:
                window.remove(nums[i-k-1])
            if v in window:
                return True
            window.add(v)  
        return False
        
"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k. 
"""
# https://leetcode.com/discuss/65056/java-python-one-pass-solution-o-n-time-o-n-space-using-buckets
# https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        bucket = {}
        width  = t+1
        
        for i in range(len(nums)):
            bIndex = nums[i]/width
            print bIndex
            if bIndex in bucket:
                return True
            if (bIndex-1) in bucket and abs(bucket[bIndex-1] - nums[i]) < width:
                return True
            if (bIndex+1) in bucket and abs(bucket[bIndex+1] - nums[i]) < width:
                return True
            bucket[bIndex] = nums[i]
            if i >= k:
                bucket.pop(nums[i-k]/width)
        return False
        
         
