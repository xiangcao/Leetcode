"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        maximumIncluding=[0 for i in range(len(nums))]
        maximumEnding=[0 for i in range(len(nums))]
        maximumEnding[0] = nums[0]
        maximumEnding[1] = max(nums[0], nums[1])
        maximumIncluding[0] = nums[0]
        maximumIncluding[1] = nums[1]
        for i in range(2, len(nums)):
            maximumIncluding[i] = maximumEnding[i-2] + nums[i]
            #maximumEnding[i] = max(maximumEnding[i-2] + nums[i], maximumIncluding[i-1])  #accepted
            #maximumEnding[i] = max(maximumIncluding[i], maximumIncluding[i-1])           #accepted
            maximumEnding[i] = max(maximumEnding[i-2] + nums[i], maximumEnding[i-1])
        return maximumEnding[-1]
      
    def rob(self, nums):
        #total0: up to but not including current item
        #total1: up to and includeing current item
        total0,total1 = 0,0
        for item in nums:
            total0,total1 = max(total0,total1), total0+item  #这样的好处很明显
        return max(total1,total0) 
    
    def rob(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)
 
#http://bookshadow.com/weblog/2015/04/01/leetcode-house-robber/

