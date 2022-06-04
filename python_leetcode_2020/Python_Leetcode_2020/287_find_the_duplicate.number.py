"""Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

https://keithschwarz.com/interesting/code/?dir=find-duplicate
class Solution:
    #binary search
    def findDuplicate1(self, nums: List[int]) -> int:
        lo = 1
        hi = len(nums) - 1
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo

    #Use Original array as Hash (element is stored as array index)
    def findDuplicate2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            pos = abs(nums[i])-1
            if nums[pos] > 0:
                nums[pos] *= -1
            else:
                return pos+1
    
    #Cyclic Sort
    def findDuplicate(self, nums: List[int]) -> int:  
        # for i in range(len(nums)):
        i = 0
        while nums[nums[i]] != nums[i]:
                tmp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = tmp
        return nums[0]
            
