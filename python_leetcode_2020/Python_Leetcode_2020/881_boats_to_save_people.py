"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 
"""

class Solution(object):
    # Two pointer, greedy
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people)-1
        boat = 0
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
                boat += 1
            else:
                j -= 1
                boat += 1
        
        return boat + 1 if i == j else boat
        

"""
Approach 1: Greedy (Two Pointer)
Intuition

If the heaviest person can share a boat with the lightest person, then do so. Otherwise, the heaviest person can't pair with anyone, so they get their own boat.

The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.

Algorithm

Let people[i] to the currently lightest person, and people[j] to the heaviest.

Then, as described above, if the heaviest person can share a boat with the lightest person (if people[j] + people[i] <= limit) then do so; otherwise, the heaviest person sits in their own boat.
"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans
