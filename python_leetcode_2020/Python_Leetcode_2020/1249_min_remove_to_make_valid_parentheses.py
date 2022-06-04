"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

Hint:
Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.

Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.

"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        def removeInvalidRightParenth(s, parenth='()'):
            result = []
            balance = 0
            for i in range(len(s)):
                if s[i] == parenth[0]:
                    balance += 1
                elif s[i] == parenth[1]:
                    balance -= 1
                if balance < 0:
                    balance = 0
                    continue
                result.append(s[i]) 
            return "".join(result)
        s = removeInvalidRightParenth(s, parenth='()')
        s = removeInvalidRightParenth(s[::-1], parenth=')(')
        return s[::-1]


# 2nd round
class Solution(object):
    #184 ms
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        def removeInvalidRight(s, brackets='()'):
            count = 0
            ans = []
            for c in s:
                if c == brackets[0]:
                    count += 1
                elif c == brackets[1]:
                    count -= 1
                if count < 0:
                    count += 1
                    continue
                else:
                    ans.append(c)
            return "".join(ans)
        s = removeInvalidRight(s, '()')
        s = removeInvalidRight(s[::-1], ')(')
        return s[::-1]

    # 88 ms > 98.43; use a stack to record the mismatching brackets
    def minRemoveToMakeValid2(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = list(s)
        stack = []
        for i, c in enumerate(ans):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    ans[i] = ''
        for extra in stack:
            ans[extra] = ''
        return "".join(ans)
