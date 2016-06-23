class Solution(object):
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
               return True
               
           if nums[middle] > nums[left]:
               if nums[left] <= target < nums[middle]:
                   right = middle - 1
               else:
                   left = middle + 1
               
           elif nums[middle] < nums[left]:
               if nums[middle] < target <= nums[right]:
                   left = middle + 1
               else:
                   right = middle - 1
           else:
               left += 1
       return False
        
