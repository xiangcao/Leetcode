class Solution:
    # 2328 ms; DP 
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = total // 2
        dp = [[False for j in range(total+1)] for i in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, total+1):
                dp[i][j] = dp[i-1][j]
                if not dp[i][j] and j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
    
    # 40 ms; use the same code for Partition to k subset equal sum
    def canPartition2(self, nums: List[int]) -> bool:
        return self.canPartitionKSubsets(nums, 2)
    
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total/k
        
        def partition(total_array, target):
            if not nums: return True
            val = nums.pop()
            for i in range(len(total_array)):
                if total_array[i] + val <= target:
                    total_array[i] += val
                    if partition(total_array, target): return True
                    total_array[i] -= val
                if total_array[i] == 0:
                    break
            nums.append(val)
            return False
        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return partition([0] * k, target)

# round 2
    # 1884 ms; DP
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        N = len(nums)
        if total % 2 != 0:
            return False
        targetSum = total // 2
        dp = [[False] * (targetSum+1) for _ in range(N+1)]
        dp[0][0] = True
        for i in range(1, N+1):
            cur = nums[i-1]
            for j in range(targetSum+1):
                if j >= cur:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-cur]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[N][targetSum]

    # 476 ms Meomization
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        N = len(nums)
        if total % 2 != 0:
            return False
        targetSum = total // 2
        memo = [[None] * (targetSum+1) for _ in range(N)]
        def dfs(subsetSum, index):
            if subsetSum == 0:
                return True
            if index == 0 or subsetSum < 0:
                return False
            if memo[index][subsetSum] is not None:
                return memo[index][subsetSum]
            result = dfs(subsetSum - nums[index], index-1) or dfs(subsetSum, index-1)
            memo[index][subsetSum] = result
            return result
        return dfs(targetSum, N-1)
