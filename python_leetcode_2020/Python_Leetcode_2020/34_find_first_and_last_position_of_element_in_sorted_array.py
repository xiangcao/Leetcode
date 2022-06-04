"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)
        # find first position of target
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        result=[]
        result.append(l)
        
        # find first position that's larger than target
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        result.append(l-1)
        return result
            

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        if l == len(nums) or nums[l] != target:
            return [-1, -1]
        result=[]
        result.append(l)
        
        r = len(nums)-1 # // We don't have to set l to 0 the second time.
        # Find the last position
        while l < r:
            mid = l + (r - l + 1) // 2 # Biased to the right
            if nums[mid] == target: # so it will get stuck at the mid
                l = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        result.append(l)
        return result
            

# third round
class Solution:
    """
    Input: [5,7,7,8,8,10]  6
    Output:  [1,1]
    Expected:  [-1,-1]

    Input: [], 0
    Output: [-1, -1]

    Input: [2,2], 2
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #first element that is >= target
        #last element that is <= target or find first element that is > target then check previous element
        
        # find first element that satisfies certian condition
        def search(nums, condition):
            left = 0
            right = len(nums)-1
            while left < right:
                mid = left + (right-left) // 2
                if condition(nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            return left
        if not nums:
            return [-1, -1]
        first_equal_to_target = search(nums, lambda x: x >= target)
        if nums[first_equal_to_target] != target:
            return [-1, -1]
        first_larger_than_target = search(nums, lambda x: x > target)
        if nums[first_larger_than_target] > target:
            last_equal_to_target = first_larger_than_target - 1
        else:
            last_equal_to_target = first_larger_than_target
        return [first_equal_to_target, last_equal_to_target]
        
