"""
 Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #refer https://leetcode.com/discuss/72216/share-some-analysis-and-explanations
        
        nums = [1] + [i for i in nums if i > 0] + [1]
        
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        
        n = len(nums)
        for length in range(2, n):
            for left in range(n-length):
                right = left + length 
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], dp[left][i] + nums[left]*nums[i]*nums[right] + dp[i][right])
                    
        return dp[0][n-1]
                
        
