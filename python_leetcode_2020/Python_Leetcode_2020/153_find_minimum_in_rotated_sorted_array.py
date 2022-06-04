"""
All the integers of nums are unique: No duplicates
"""
class Solution:
    # Binary search
    def findMin1(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        return nums[left]

    # this solution can be easily adapted to handle duplicates
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]                

class Solution:
    # find the first element that is smaller than nums[0]
    def findMin(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right > left:
            # Find the mid element
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]: # = is for the case of only two element[4,3]
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
