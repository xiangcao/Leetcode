"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2


Example 3:
Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:        
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


   
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        """We will partition the array into two sides, with one copy of each number
on the left, in order, as far as possible. [1, 2, 3, 4, 5, ..., n][...(everything else, but not n+1)...]."""
        i = 0
        end = len(nums)
        """Call LeftPartition the interval [1, ..., i - 1]
        Call RightPartition the interval [nums[end], nums[-1].
        Initially, both are empty.
            At the end, when "i" and "end" meet, call the results FinalLeftPartition and FinalRightPartition.
        Then the answer to the problem is 1 + size(FinalLeftPartition).
        We build those intervals in-place, by swapping elements when necessary, and updating i and end.
        """
        while (i != end):
            int val = nums[i];
            if (val == 1 + i): # Number is in the right place. We may consider it part of LeftPartition, and advance i.
                i += 1
            elif (val > end # If this should go in FinalLeftPartition, then that would overlap with FinalRightPartition.
                or val <= 0 # The number is negative, it cannot possibly belong in FinalLeftPartition.
                or nums[val - 1] == val # This is a duplicate. It doesn't belong in FinalLeftPartition. 
                  #How can we get away with checking just this one spot for a duplicate?
                  # See the next "else" branch -- we always put values into this exact spot.
                #If any of the above statements is true, this value doesn't need to be in FinalLeftPartition.
                #So we may put it in the right partition,
                #and advance "end".
                swap(nums[i], nums[--end]);
                #Now nums[i] has some new value that we haven't considered before, so
                #leave "i" as is and go back to the top of the loop.
            else:
                # We don't yet know whether val should be in
                # FinalLeftPartition or FinalRightPartition, so put it in neither.
                # In order to consider another value, place val so that it matches its own index;
                # that is, place it where it will be if indeed it ends up in FinalLeftPartition,
                # and next consider the element there.
                swap(nums[i], nums[val - 1]);
                # We learned nothing new about what elements will be in FinalLeftPartition or FinalRightPartition,
                # and nums[i] has the previous value of nums[val - i], which we haven't dealt with yet,
                # so continue the loop without advancing either pointer.
                # But we did make useful progress in this branch: now in the future, if we see the same "val"
                # again, we will know it's a duplicate, because of the "nums[val - 1] == val" check above!
        return i + 1


# 
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Base case.
        if 1 not in nums:
            return 1
        
        # nums = [1]
        if n == 1:
            return 2
        
        # Replace negative numbers, zeros,
        # and numbers larger than n by 1s.
        # After this convertion nums will contain 
        # only positive numbers.
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        # Use index as a hash key and number sign as a presence detector.
        # For example, if nums[1] is negative that means that number `1`
        # is present in the array. 
        # If nums[2] is positive - number 2 is missing.
        for i in range(n): 
            a = abs(nums[i])
            # If you meet number a in the array - change the sign of a-th element.
            # Be careful with duplicates : do it only once.
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
            
        # Now the index of the first positive number 
        # is equal to first missing positive.
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
            
        return n + 1
