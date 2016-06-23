"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13. 
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        rearsize = 1
        mod = 1
        while mod <= n:
            rear =  n % mod
            front  = n / (mod * 10)
            curdigit = (n / mod) % 10
            
            if curdigit > 1:
                count += (front + 1 ) * rearsize
            elif curdigit == 1:
                count += front * rearsize + rear + 1
            else:
                count += front * rearsize
            mod *= 10
            rearsize *= 10
        return count
            
            
#Very Easy to Understand Java Solution 0ms. 附中文解释
# https://leetcode.com/discuss/85529/very-easy-to-understand-java-solution-0ms-%E9%99%84%E4%B8%AD%E6%96%87%E8%A7%A3%E9%87%8A 
