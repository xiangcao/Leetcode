class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            if i == 0:
                continue
            for j in range(i):
                dp[i, A[i]-A[j]] = dp.get((j, A[i]-A[j]), 1) + 1
        return max(dp.values())

     # as a reference, this is the dp code for longest incrementing subsequence
    # DP O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * (len(nums))
        dp[0] = 1
        for i, n in enumerate(nums):
            if i == 0:
                continue
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            dp[i] = max(dp[i], 1)
        return max(dp)
