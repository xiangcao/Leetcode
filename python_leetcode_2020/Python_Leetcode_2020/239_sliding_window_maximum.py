"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?
"""

class Solution(object):
    # Another way of explaining the deque method (approach 2): You want to ensure the deque window only has decreasing elements. That way, the leftmost element is always the largest.
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        deq = collections.deque()
        def add(i):
            if deq and deq[0] <= i - k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
        
        for i in range(k):
            add(i)
        result = [nums[deq[0]]]
        
        for i in range(k, n):
            add(i)
            result.append(nums[deq[0]])
        return result

    #[1], k=1
    # [7,2,4] 2
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        def add(i):
            if window and i - window[0] >= k:
                window.popleft()
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        
        for i in range(k):
            add(i)
        result = []
        for j in range(k, len(nums)):
            result.append(nums[window[0]])
            add(j)
        #need to get max from window one more time after the loop ended. 
        #this is because the loop above get max from the window before add(j) is inovked. 
        # compare with the solution above. the solution above do not need to invoke result.append(nums[window[0]]) one more time after loop ended
        result.append(nums[window[0]])
        return result
