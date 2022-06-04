"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # Brute force: O(N^2)
    def longestConsecutive1(self, nums: List[int]) -> int:
        longest_streak = 0
        nums = set(nums)
        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    # Improved to O(N) by only building sequences from numbers that are not already part of a longer sequence. 
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums = set(nums)
        for num in nums:
            # this improved time from O(N^2) to O(N)
            if num - 1 in nums:  
                continue
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    # Sort: O(NLogN)
    def longestConsecutive3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        cur_len = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                cur_len += 1
            else:
                ans = max(ans, cur_len)
                cur_len = 1
        return max(ans, cur_len)
            
                
                
# round 2
First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.

def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for n in nums:
            if n-1 in nums:
                continue
            cur_n = n
            while cur_n + 1 in nums:
                cur_n = cur_n + 1
            best = max(best, cur_n - n + 1)
        return best
