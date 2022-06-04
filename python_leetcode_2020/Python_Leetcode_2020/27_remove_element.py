"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    # Approach 1: Two Pointers
    # consider the elements to be removed as non-existent. In a single pass, if we keep copying the visible elements in-place, that should also solve this problem for us.
    def removeElement1(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
    
    #Approach 2: Two Pointers - when elements to remove are rare
    # We can move all the occurrences of this element to the end of the array.
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while (i < n):
            if (nums[i] == val):
                nums[i] = nums[n - 1]
                #reduce array size by one
                n -= 1
            else:
                i += 1
            
        return n
