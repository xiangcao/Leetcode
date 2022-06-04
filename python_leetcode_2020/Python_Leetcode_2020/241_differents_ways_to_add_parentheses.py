"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""

# same algorithm as leetcode 95 Unique BST trees II
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.memoization = {}
        return self.allResults(input)
    
    def allResults(self, input: str):
        if input in self.memoization:
            return self.memoization[input]
        if input.isdigit():
            return [int(input)]
        
        result = []
        
        for i,c in enumerate(input):
            if c in '+-*':
                leftResults = self.allResults(input[:i])
                rightResults = self.allResults(input[i+1:])
                for l in leftResults:
                    for r in rightResults:
                        if c == '+':
                            result.append(l + r)
                        elif c == '-':
                            result.append(l - r)
                        else:
                            result.append(l * r)
        self.memoization[input] = result
        return result
        
