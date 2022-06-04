"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i = 0 
        while i < len(asteroids):
            a = asteroids[i]
            if not stack or a > 0 or stack[-1] < 0:
                stack.append(a)
            else:
                prev = stack[-1]
                if abs(prev) > abs(a):
                    pass
                elif abs(prev) == abs(a):
                    stack.pop()
                else: # abs(prev) < abs(a):
                    stack.pop()
                    i -= 1
            i += 1
        return stack
                    
