"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        #Radix Sort
        def countSort(nums, exp):
            aux=[0] * len(nums)
            count=[0] * 10
            for i in nums:
                count[(i/exp)%10] += 1
        
            for i in range(1,10):
                count[i] += count[i-1]
            
            for i in range(len(nums)-1, -1, -1):
                elem = nums[i]
                count[(elem/exp)%10] -= 1
                aux[ count[(elem/exp)%10]] = elem
            for i in range(len(nums)):
                nums[i] = aux[i]
        
        exp =  1
        maximum = max(nums)
        while maximum/exp > 0:
            countSort(nums, exp)
            exp *= 10
        
        maxGap = 0 
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            maxGap = max(maxGap, diff)
        return maxGap
            
