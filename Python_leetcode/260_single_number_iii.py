"""
https://leetcode.com/discuss/52351/c-o-n-time-o-1-space-9-line-solution-with-detail-explanation
good post explaining 2's complement for negative integers:
http://stackoverflow.com/questions/14326900/how-does-c-do-bitwise-or-operations-on-negative-numbers

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =[0,0]
        different = 0
        for i in nums:
            different ^= i
        
        #last bit set
        different &= (-different)
            
        for i in nums:
            if i & different:
                result[0] ^= i
            else:
                result[1] ^= i

        return result
        
