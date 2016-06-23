"""
 There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
"""


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # number of factors for each i, from 1 to i. 
        # = number of toggle
        # odd number of toggle: on
        # even number of toggle: off
        
        #1: 1
        #2: 1, 2
        #3: 1, 3
        #4: 1, 2, 4
        #5: 1, 5
        #6: 1, 2, 3, 6
        #7: 1, 7
        #8: 1, 2, 4, 8
        #9: 1, 3, 9
        return int(math.sqrt(n))
        
        
        
