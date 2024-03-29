"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        result=[0] * len(T)
        
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                pos = stack.pop()
                result[pos] = i - pos
            stack.append(i)
        return result
            
        

# round 2
class Solution:
    # Monotonic Stack
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack=[]
        result=[0] * len(T)
        for i, t in enumerate(T):
            if not stack or t <= T[stack[-1]]:
                stack.append(i)
            else:
                while stack and t > T[stack[-1]]:
                    prev_day = stack.pop()
                    result[prev_day] = i - prev_day
                stack.append(i)
        return result
                

