class Solution:
    """As in Approach #2, let's binary search for the answer, and we will focus on evaluating our possible function quickly.
    
Algorithm

We will use a sliding window approach to count the number of pairs with distance <= guess.

For every possible right, we maintain the loop invariant: left is the smallest value such that nums[right] - nums[left] <= guess. Then, the number of pairs with right as it's right-most endpoint is right - left, and we add all of these up."""
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
    
    def smallestDistancePair2(self, nums: List[int], k: int) -> int:
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            return sum(prefix[min(x + guess, W)] - prefix[x] + multiplicity[i]
                       for i, x in enumerate(nums)) >= k

        nums.sort()
        W = nums[-1]

        #multiplicity[i] = number of nums[j] == nums[i] (j < i)
        multiplicity = [0] * len(nums)
        for i, x in enumerate(nums):
            if i and x == nums[i-1]:
                multiplicity[i] = 1 + multiplicity[i - 1]

        #prefix[v] = number of values <= v
        prefix = [0] * (W + 1)
        left = 0
        for i in range(len(prefix)):
            while left < len(nums) and nums[left] <= i:
                left += 1
            prefix[i] = left

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo
