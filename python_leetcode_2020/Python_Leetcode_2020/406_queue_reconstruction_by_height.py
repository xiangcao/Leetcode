"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
"""

#shortest person is invisible to higher person in terms of k
#but higher person is visible to shorter person
#so we can arrange higher person first

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda p: (-p[0], p[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        
        return output
