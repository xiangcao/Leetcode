"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

"""

class Solution(object):
    # Two sum
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        c = [0] * 60
        res = 0
        for t in time:
            complement = (60-t % 60) % 60
            res += c[complement]
            c[t % 60] += 1
        return res
