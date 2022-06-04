"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
"""

class Solution(object):
    
    #Approach 1 O(N):
    def missingElement1(self, nums, k):
        n=nums.size()
        diff=0
        for i in range(1,n):
            diff=nums[i]-nums[i-1]-1
            if(diff>=k):
                return nums[i-1]+k
            k-=diff
        return nums[n-1]+k
    
    # Approach 2
    """Intuition
    The idea is to find the leftmost element such that the number of missing numbers until this element is less or equal to k.
    """
    def missingElement(self, nums, k):
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx

        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left != right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot 
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left]
        return nums[left - 1] + k - missing(left - 1) 

    """
    Let missingNum be amount of missing number in the array. Two cases that need to be handled:

    missingNum < k, then return nums[n - 1] + k - missingNum
    missingNum >= k, then use binary search(during the search k will be updated) to find the index in the array, where the kth missing number will be located in (nums[index], nums[index + 1]), return nums[index] + k"""
    def missingElement2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, l, h = len(nums), 0, len(nums)-1
        missingNum = nums[n - 1] - nums[0] -(n-1)

        if (missingNum < k):
            return nums[n - 1] + k - missingNum
        
        while (l < h - 1):
            m = l + (h - l) // 2
            missing = nums[m] - nums[l] - (m - l)
            if (missing >= k):
			    # when the number is larger than k, then the index won't be located in (m, h]
                h = m
            else:
			    # when the number is smaller than k, then the index won't be located in [l, m), update k -= missing
                k -= missing
                l = m

        return nums[l] + k
