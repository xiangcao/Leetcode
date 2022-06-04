"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)
