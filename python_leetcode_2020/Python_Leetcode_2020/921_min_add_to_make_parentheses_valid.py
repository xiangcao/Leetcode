"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""

class Solution:
    """
    Intuition and Algorithm

Keep track of the balance of the string: the number of '(''s minus the number of ')''s. A string is valid if its balance is 0, plus every prefix has non-negative balance.

The above idea is common with matching brackets problems, but could be difficult to find if you haven't seen it before.

Now, consider the balance of every prefix of S. If it is ever negative (say, -1), we must add a '(' bracket. Also, if the balance of S is positive (say, +B), we must add B ')' brackets at the end.
    """
    def minAddToMakeValid(self, S: str) -> int:
        ans = balance = 0
        for symbol in S:
            balance += 1 if symbol == '(' else -1
            if balance == -1:
                ans += 1
                balance = 0
        return ans + balance

# round 2
    def minAddToMakeValid(self, S: str) -> int:
        ans = 0
        count = 0
        for c in S:
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                ans -= count
                count = 0
        ans += count
        return ans
