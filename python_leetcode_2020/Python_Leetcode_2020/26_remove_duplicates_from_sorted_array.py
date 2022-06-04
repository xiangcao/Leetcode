class Solution:
    """Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""
    def removeDuplicates1(self, nums: List[int]) -> int:
        begin = 0
        for i, n in enumerate(nums):
            if i == 0:
                begin += 1
                continue
            if nums[i] == nums[i-1]:
                continue
            nums[begin] = nums[i]
            begin += 1
        return begin
    
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i + 1
            
