"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        maxLen = 0
        left = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        maxLen = max(maxLen, i-stack[-1])
                    else:
                        maxLen = max(maxLen, i-left)
                else:
                    left = i
        return maxLen

"""
Instead of finding every possible string and checking its validity, we can make use of stack while scanning the given string to check if the string scanned so far is valid, and also the length of the longest valid string. In order to do so, we start by pushing −1 onto the stack.

For every ‘(’ encountered, we push its index onto the stack.

For every ‘)’ encountered, we pop the topmost element and subtract the current element's index from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.

See this example for better understanding.
"""
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        maxLen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:   
                    maxLen = max(maxLen, i-stack[-1])
                else:
                    stack.append(i)
        return maxLen

# Approach 4: O(1) space
# In this approach, we make use of two counters left and  right to track the valid string length in one direction
# Then, traveral string in both direction; first time from beginning to end; second time reverse it
