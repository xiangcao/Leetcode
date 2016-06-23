class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) /2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] < target: 
            #there is no element larger than target in nums[:]. so should append to the end. 
            left += 1
        return left
        
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) /2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1 

        return left
