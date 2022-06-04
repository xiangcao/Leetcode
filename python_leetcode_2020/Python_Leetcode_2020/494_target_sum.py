"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

DP solution
dp[i][j] refers to the number of assignments which can lead to a sum of jj upto the i^th index. To determine the number of assignments which can lead to a sum of sum + nums[i] upto the (i+1)^{th} index, we can use dp[i][sum + nums[i]] = dp[i][sum + nums[i]] + dp[i-1][sum]. Similarly, dp[i][sum - nums[i]] = dp[i][sum + nums[i]] + dp[i-1][sum]. We iterate over the dp array in a rowwise fashion i.e. Firstly we obtain all the sums which are possible upto a particular index along with the corresponding count of assignments and then proceed for the next element(index) in the numsnums array.

But, since the sumsum can range from -1000 to +1000, we need to add an offset of 1000 to the sum indices (column number) to map all the sums obtained to positive range only.

At the end, the value of dp[n-1][S+1000]dp[n−1][S+1000] gives us the required number of assignments. Here, nn refers to the number of elements in the numsnums array.

The animation below shows the way various sums are generated along with the corresponding indices. The example assumes sumsum values to lie in the range of -6 to +6 just for the purpose of illustration. This animation is inspired by @Chidong
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        mapping = [dict() for _ in range(len(nums))]
        def dfs(index, target):
            if index == len(nums):
                return target == 0
            if target not in mapping[index]:
                mapping[index][target] = dfs(index+1, target-nums[index]) + dfs(index+1, target+nums[index])
            return mapping[index][target]
        return dfs(0, S)
    
    #brute force
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def dfs(index, target):
            if index == len(nums):
                return target == 0
            return dfs(index+1, target-nums[index]) + dfs(index+1, target+nums[index])
        return dfs(0, S)

    # DP 
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # int[][] dp = new int[nums.length][2001];
        dp=[[0] * 2001 for _ in range(len(nums))]
        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1

        for i in range(1, len(nums)):
            for sum in range(-1000, 1001):
                if (dp[i - 1][sum + 1000] > 0):
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000]
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000]
        return dp[len(nums) - 1][S + 1000] if S<= 1000 else 0
