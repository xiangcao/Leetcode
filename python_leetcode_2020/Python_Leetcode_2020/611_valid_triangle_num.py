"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            # Notes 
            # we should either skip 0 elements; or we have to make sure k always larger than j; this is important because we doesn't change k after j increments; if j is equal to k, we are comparing num[i] + nums[k]  and nums[k]
            
            # if nums[i] == 0: continue 
            
            k = i + 2
            for j in range(i+1,len(nums)-1):
                while (k <= j or (k < len(nums) and nums[i] + nums[j] > nums[k])):
                    k+= 1
                count += k - j - 1
        return count


class Solution:
    # sort first;
    #time: O(N^2); 
    # space: O(LogN) for sorting
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums) and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
        return count
