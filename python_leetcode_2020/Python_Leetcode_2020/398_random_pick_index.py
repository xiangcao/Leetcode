"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.
"""
# explanation: https://aaronice.gitbook.io/lintcode/random/random-pick-index
# Reservoir Sampling
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0 # count also is the index of incoming item to be considered to be picked or not
        ans = -1
        k = 1
        for i, value in enumerate(self.nums):
            if value == target:
                if random.randrange(count+1) < k:
                    ans = i
                count += 1
        return ans
