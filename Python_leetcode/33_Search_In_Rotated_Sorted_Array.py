class Solution(object):
    
   #correct
   def _binarySearch(self,nums, left, right, func):
       while left <= right:
           mid = (left + right) / 2
           if func(mid):
               right = mid - 1
           else:
               left = mid + 1
       return left
       # left always return the first element for which func(x) to be true
       
       # 8,7,3,4,5
       # left: 0, right:4, 
       # mid: 2, func(2):  nums[2] <= nums[-1] is True. therefore, left = 0, right=1
       # mid: 0, func(0): nums[0] <= nums[-1] is False. therefore, left = 1, right=1
       # mid: 1, func(1): nums[1] <= nums[-1] is False. therefore, left =2, right =1. break while loop
       # return left which is 2. correct
       
       
       #1
       #left 0 right 0
       # mid: 0, func(0): nums[0] <= nums[-1] is True. left=0, right = -1
       
   #correct       
   def _binarySearch(self,nums, left, right, func):
       while left < right:
           mid = (left + right) / 2
           if func(mid):
               right = mid 
           else:
               left = mid + 1
       return left
       
       
       # time limit exceeded
       '''
       def _binarySearch(self,nums, left, right, func):
          while left <= right:
             mid = (left + right) / 2
                if func(mid):
                   right = mid
                else:
                   left = mid + 1
          return left
       # 8,7,3,4,5
       # left: 0, right:4, 
       # mid: 2, func(2):  nums[2] <= nums[-1] is True. therefore, left = 0, right=2
       # mid: 1, func(0): nums[1] <= nums[-1] is False. therefore, left = 2, right=2
       # mid: 2, func(1): nums[1] <= nums[-1] is True. therefore, left = 2, right=2
       # return left
       
       '''

# find first number >= 5
#1,3,5,7,9
# func: >=5
# lambda mid: nums[mid] >=5 


   def search_(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: int
       """
       # find the index of first element in increasing sequence
       shiftIndex = self._binarySearch(nums, 0, len(nums) - 1, lambda mid: nums[mid] <= nums[-1])

       # index: index for array before rotation
       # mappingIndex(index): index for array after rotation
       mappingIndex = lambda index: (index + shiftIndex) % len(nums)

       # find the index of first element larger or equal to target in the array before rotation.
       originalIndex = self._binarySearch(nums, 0, len(nums) - 1, lambda mid: nums[mappingIndex(mid)] >= target)
       
       currIndex = mappingIndex(originalIndex)

       if nums[currIndex] == target:
          return currIndex

       return -1
       
   def search(self, nums, target):
       """
       :type nums: List[int]
       :type target: int
       :rtype: int
       """
       left = 0
       right = len(nums) - 1
       
       while left <= right:
           middle = left + (right-left)/2
           if nums[middle] == target:
               return middle
               
           if nums[middle] >= nums[left]:
               if nums[left] <= target < nums[middle]:
                   right = middle - 1
               else:
                   left = middle + 1
               
           elif nums[middle] <= nums[right]:
               if nums[middle] < target <= nums[right]:
                   left = middle + 1
               else:
                   right = middle - 1
       return -1
       
