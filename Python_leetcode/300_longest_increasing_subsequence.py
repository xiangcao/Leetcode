class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://docs.python.org/2/library/bisect.html
        #O(nlogn)
        # refer https://leetcode.com/discuss/67609/short-java-solution-using-dp-o-n-log-n
        """
        The basic idea is present in the majority of solutions shared for this task, I have only tried to implement it in a manner as concise as possible without damaging the code readability.
        
       The idea is that as you iterate the sequence, you keep track of the minimum value a subsequence of given length might end with, for all so far possible subsequence lengths. So dp[i] is the minimum value a subsequence of length i+1 might end with. Having this info, for each new number we iterate to, we can determine the longest subsequence where it can be appended using binary search. The final answer is the length of the longest subsequence we found so far.
        """
        # same idea with http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        # So dp[i] is the minimum value a subsequence of length i+1 might end with 
        dp = [0] *len(nums)
        
        maxLen = 0
        
        for x in nums:
            # get the insert position. the first element that is equal or larger than x
            # subsequences of length less than (insert+1) has an min ending value less than x
            # subsequences of length >= (insert+1) has an ending value >= x
            insert = bisect.bisect_left(dp, x, 0, maxLen)  
            dp[insert] = x
            # if insert equal to maxLen, it means all subsequences with length (0~maxLen) ends with an element less than x. so we can extend the length of longest increasing sequence so far to be maxLen+1 (or, insert+1)
            if insert == maxLen:
                maxLen += 1
        return maxLen
        
    #another similar nlogn solution : https://leetcode.com/discuss/67554/9-lines-c-code-with-o-nlogn-complexity
    
        
    def lengthOfLIS(self, nums):
        #O(n^2). DP
        #dp[i] be the length of the LIS till index i 
        if not nums:
            return 0
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
