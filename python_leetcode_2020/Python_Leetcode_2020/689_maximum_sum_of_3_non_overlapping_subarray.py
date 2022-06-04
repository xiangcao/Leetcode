"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
"""

class Solution:
    # DP
    # W: is a sliding window of k recording the sum of each window
    # left[i] records the first occurnce of the largest value of W[z] in the interval [0, i] (0<=z<=i) 
    # right[i] records the first occurence of the largest value of W[z] in the interval of [i,len(W)-1]
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        W = [] #array of sums of window
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if i >= k:
                cursum -= nums[i-k]
            if i >= k-1:
                W.append(cursum)
        left=[0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best
        right=[0] * len(W)
        best = len(W) - 1
        for i in reversed(range(len(W))):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(nums)-2*k+1):
            first = left[j - k]
            third = right[j + k]
            if ans is None or (W[first] + W[j] + W[third]) > (W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = [first, j, third]
        return ans
            

# Space O(1) solution
A greedy solution using three sliding windows where you keep track of the best indexes/sums as you go.

O(n) time: Since we're only going through the list once and using no complex operations, this is O(n).
O(1) space: Just a fixed set of temp vars. We don't need the extra arrays that the DP solutions have.

class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k*2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k*2])
        seqThreeSum = sum(nums[k*2:k*3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k*2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq
