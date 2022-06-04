"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.
"""

class Solution:
    # binary search
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            left_length = mid - left
            if left_length % 2 == 1:
                if nums[mid] == nums[mid+1]:
                    right = mid - 1
                elif nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid+1]:
                    left = mid 
                elif nums[mid] == nums[mid-1]:
                    right = mid
                else:
                    return nums[mid]
        return nums[left]
            
