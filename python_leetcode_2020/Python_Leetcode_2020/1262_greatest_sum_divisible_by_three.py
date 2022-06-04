"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

Constraints:

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

"""
class Solution:
    # Recursive; Time exceeded
    def maxSumDivThree1(self, nums: List[int]) -> int:
        def recursive(i, remainder):
            if i == 0:
                return nums[i] if nums[i] % 3 == remainder else 0
            cur_remainder = nums[i] % 3
            return max(recursive(i-1, remainder), recursive(i-1, (remainder - cur_remainder) % 3)+nums[i])
        return recursive(len(nums)-1, 0)

    # seen[i] means the current maximum possible sum that sum % 3 = i
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
        return seen[0]
    
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(nums))]
        
        dp[0][0] = nums[0] if nums[0] % 3 == 0 else 0
        dp[0][1] = nums[0] if nums[0] % 3 == 1 else float("-inf")
        dp[0][2] = nums[0] if nums[0] % 3 == 2 else float("-inf")

        for i in range(1, len(nums)):
            cur_remainder = nums[i] % 3
            for k in range(3):
                dp[i][k] = max(dp[i-1][k], dp[i-1][(k - cur_remainder)%3] + nums[i])
        return dp[-1][0]

"""
Explanation (from leetcode):
So the state here is dp[i][m]. dp[i][m] = largest sum from a subset of nums[:i] such that the sum % 3 equals m. After defining this we loop thru each number in nums. At each number we mod it by 3 and see what the result is.

For example, lets say the current number (nums[i]) we're looking at is 4. 4 % 3 = 1. So what does this mean? For each of the states we're tracking (dp[i][0], dp[i][1], dp[i][2]) how can we use this? If we add a number with remainder 1 to a sum with remainder 1 what do we get? We get a number with remainder 2. So we can use this info to construct the answer!

Example: If nums[i] % 3 == 1. We have remainder 1. How can we use this?:

For dp[i][0] we want a remainder of 0. How do we get this given we currently have a remainder of 1? We can add this number with remainder 1 to a sum with remainder 2. This creates an overall remainder of 0 as 2 + 1 = 3
For dp[i][1] we want a remainder of 1. This means we can add this number to dp[i-1][0]. This will give an overall remainder of 1 (num_with_remainder_0 + num_with_remainder_1) % 3 = 1.
For dp[i][2] we do the same thing. We can add the number to dp[i][1]. Why? If you've been following you can probably answer now.
We do this for each of the three cases:

if num % 3 == 0
if num % 3 == 1
if num % 3 == 2
And we're done.

def maxSumDivThree(self, nums: List[int]) -> int:
	n = len(nums)
	dp = [[0]*3 for _ in range(n+1)]
	dp[0][1] = float('-inf')
	dp[0][2] = float('-inf')
	for i in range(1, n+1):
		if nums[i-1] % 3 == 0: # Current remainder == 0
			dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][0] to keep the remainder 0
			dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][1] to keep the remainder 1
			dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1]) # Current remainder is 0, so we add to dp[i-1][2] to keep the remainder 2
		elif nums[i-1] % 3 == 1: # Current remainder == 1
			dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][2] to keep the remainder 0
			dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][0] to keep the remainder 1
			dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1]) # Current remainder is 1, so we add to dp[i-1][1] to keep the remainder 2
		else: # Current remainder == 2
			dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1]) # Can you tell how this works now?
			dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
			dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

	return dp[-1][0]
"""
