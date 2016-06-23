"""
generalized solution:
https://leetcode.com/discuss/31595/detailed-explanation-generalization-bitwise-operation-numbers
https://leetcode.com/discuss/54970/an-general-way-to-handle-all-this-sort-of-questions


a  good solution:
https://leetcode.com/discuss/6632/challenge-me-thx


"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ones = twos = 0
        for i in nums:
            twos ^= ones & i
            ones ^= i
            mask = ~ (twos & ones)
            twos = mask & twos
            ones = mask & ones
        return ones
