"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""
class Solution:
    # time: O(K^(N-K)* K!)
    # space O(N)
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
        nums.sort() # this improved performance from 3900 ms to 100 ms
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return partition([0] * k, target)

# solution 2 in java

canPartitionKSubsets() is true when there are exactly k subsets with equal subset sum sum / k, and each element are only used once.

comparison between curSubsetSum and targetSubsetSum indicates whether we find a valid subset.
k restricts there are k subsets exactly.
We can take it as a nested recursion. The graph below shows the control flow (not accurate):

Outer recursion on k subsets:
Base case: k == 0
Recursive case: k > 0 
				// Inner recursion on individual subset
				Base case: curSubsetSum == targetSubsetSum (return to outer recursion)
				Recursive case: curSubsetSum < targetSubsetSum
Since the order of numbers within a subset doesn't matter, we add nextIndexToCheck for the inner recursion to avoid duplicate calculations.

class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = 0, maxNum = 0;
        for (int num : nums) {
            sum += num;
            maxNum = Math.max(maxNum, num);
        }
        if (sum % k != 0 || maxNum > sum / k) {
            return false;
        }
        return canPartitionKSubsetsFrom(nums, k, new boolean[nums.length], sum / k, 0, 0);
    }
    
    private boolean canPartitionKSubsetsFrom(int[] nums, 
                                             int k,
                                             boolean[] visited, 
                                             int targetSubsetSum, 
                                             int curSubsetSum, 
                                             int nextIndexToCheck) {
        if (k == 0) {
            return true;
        }
        
        if (curSubsetSum == targetSubsetSum) {
            return canPartitionKSubsetsFrom(nums, 
                                            k - 1,
                                            visited,
                                            targetSubsetSum,
                                            0,
                                            0);
        }
        
        for (int i = nextIndexToCheck; i < nums.length; i++) {
            if (!visited[i] && curSubsetSum + nums[i] <= targetSubsetSum) {
                visited[i] = true;
                if (canPartitionKSubsetsFrom(nums, 
                                             k,
                                             visited,
                                             targetSubsetSum,
                                             curSubsetSum + nums[i],
                                             i + 1)) {
                    return true;
                }
                visited[i] = false;
            }
        }
        
        return false;
    }
}





# round 2
class Solution(object):
    # dp : 928 ms; memory: 14.8 mb
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in xrange(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]
 
    # memo: 156 ms; memory: 25.5 mb
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1<<i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)
    
    # 24 ms; memory: 13.7 mb
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)
