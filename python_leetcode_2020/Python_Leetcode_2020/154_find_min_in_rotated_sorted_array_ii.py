"""
contains duplicates
"""

class Solution:
    # Average O(LogN), worst case is O(N)
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = right - 1
        return nums[left]
