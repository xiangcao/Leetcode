"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0 
        countMap = collections.Counter()
        maxLen = 0
        for index, e in enumerate(nums):
            count += 1 if e == 1 else -1;
            if count == 0:
                maxLen = max(maxLen, index + 1)
            elif count in countMap:
                maxLen = max(maxLen, index - countMap[count])
            else:
                countMap[count] = index
        return maxLen
