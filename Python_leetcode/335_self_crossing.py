"""
 You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)

Example 2:

Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)

Example 3:

Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)

"""

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        # great solution https://leetcode.com/discuss/88054/java-oms-with-explanation
        l = len(x)
        if l < 4:
            return False
            
        for i in range(3, l):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i >= 4:
                if x[i] + x[i-4] >= x[i-2] and x[i-1] == x[i-3]:
                    return True
            if i >= 5:
                if x[i-4]+x[i] >= x[i-2] and x[i-2] >= x[i-4] and x[i-5] + x[i-1] >= x[i-3] and x[i-1] <= x[i-3]:
                    return True
        return False

# stephanPochman solution: https://leetcode.com/discuss/88153/another-python
def isSelfCrossing(self, x):
    return any(d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b)
               for a, b, c, d, e, f in ((x[i:i+6] + [0] * 6)[:6]
                                        for i in xrange(len(x))))
