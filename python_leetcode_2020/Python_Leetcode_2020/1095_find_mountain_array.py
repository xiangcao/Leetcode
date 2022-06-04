# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        l, r = 0, n-1
        begin = mountain_arr.get(l)
        end = mountain_arr.get(r)
        if target == begin:
            return l
        while l < r:
            mid = l + (r-l) // 2
            mid_value = mountain_arr.get(mid)
            mid_next_value = mountain_arr.get(mid+1)
            if mid_value > mid_next_value:
                r = mid 
            else:
                l = mid + 1
        # l is the peak
        peak = l

        def binary_search_increasing(l, r):
            while l < r:
                mid = l + (r-l) // 2
                mid_value = mountain_arr.get(mid)
                if mid_value == target:
                    return mid
                elif mid_value < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1 if mountain_arr.get(l) != target else l

        def binary_search_decreasing(l, r):
            while l < r:
                mid = l + (r-l) // 2
                mid_value = mountain_arr.get(mid)
                if mid_value == target:
                    return mid
                elif mid_value < target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1 if mountain_arr.get(l) != target else l
        
        if target >= begin:
            left_result = binary_search_increasing(0, peak)
            if left_result != -1:
                return left_result 
        if target >= end:
            return binary_search_decreasing(peak+1,  n-1)     
        return -1

# round 2:
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def peakIndexInMountainArray(arr) -> int:
            left, right = 0, arr.length()-1
            while left < right:
                mid = left + (right-left)//2
                if arr.get(mid) < arr.get(mid+1):
                    left = mid + 1
                else:
                    right = mid
            return left
        N = mountain_arr.length()
        peakIndex = peakIndexInMountainArray(mountain_arr)
        
        def binarySearchLeft(mountain_arr, left, right, target):
            while left < right:
                mid = left + (right-left) // 2
                if mountain_arr.get(mid) >= target:
                    right = mid
                else:
                    left = mid + 1
            return left if mountain_arr.get(left) == target else -1
        
        def binarySearchRight(mountain_arr, left, right, target):
            while left < right:
                mid = left + (right-left) // 2
                if mountain_arr.get(mid) > target:
                    left = mid + 1
                else:
                    right = mid
            return left if mountain_arr.get(left) == target else -1
                
        leftIndex = binarySearchLeft(mountain_arr, 0, peakIndex, target)
        if leftIndex != -1:
            return leftIndex
        rightIndex = binarySearchRight(mountain_arr, peakIndex+1, N-1, target)
        return rightIndex
