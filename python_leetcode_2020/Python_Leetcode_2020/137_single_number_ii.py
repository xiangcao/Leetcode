"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_once = seen_twice = 0

        for num in nums: 
            # NOT seen_twice AND (CHANGE see_once)
            # NOT seen_once AND (CHANGE see_twice)
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once

            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice

            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once
        

    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i = 0; i < 32; i++) {
            int ones = 0;
            for (int n: nums) {
                ones += ((n >> i) & 1);
            }
            if (ones % 3 != 0) {
                ans = ans + (1 << i);
            }
        }
        return ans;
    }
