"""
Given a sorted integer array without duplicates, return the summary of its ranges.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary = []
        left = 0
        for j in range(len(nums)):
            #check if j + 1 extends the range [nums[i], nums[j]]
            if (j + 1 < len(nums) and nums[j + 1] == nums[j] + 1):
                continue
            # put the range [nums[i], nums[j]] into the list
            if (left == j):
                summary.append(str(nums[left]))
            else:
                summary.append(str(nums[left]) + "->" + str(nums[j]))
            left = j + 1
        return summary
