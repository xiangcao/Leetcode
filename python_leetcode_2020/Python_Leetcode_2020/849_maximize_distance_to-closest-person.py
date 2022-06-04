"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
"""
"""
Idea is simple. Use two pointers.

If the current value is "0", keep going forward.
Left pointer points to the position of left "1" and right pointer points to the position of right "1". Keep updating two pointers and calculate the max distance.
Be careful of two situations: seats[0] is 0 and seats[len - 1] is 0. Just check them and get the final answer. Ex: 00101000.

So the problem is to find the maximum distance between two continuous 1 in an array, and just return half of that maximum value...(also before the first 1 and after the last 1 will be two special cases)

"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left =-1
        maxDis = 0
        
        for i in range(len(seats)):
            if (seats[i] == 0): continue;

            if (left == -1):
                maxDis = max(maxDis, i)
            else:
                maxDis = max(maxDis, (i-left) // 2)
            left = i
        
        if (seats[-1] == 0):
            maxDis = max(maxDis, len(seats) - 1 - left)
        
        return maxDis
