"""
 Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = False
        k = 0 
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev:
                if not duplicate:
                    nums[k] = nums[i]
                    k += 1
                duplicate = True
            elif nums[i] != prev:
                duplicate = False
                prev = nums[i]
                nums[k] = nums[i]
                k += 1
        return k
            
        
