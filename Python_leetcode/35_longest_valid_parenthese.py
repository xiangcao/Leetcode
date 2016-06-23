class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0 
        stack=[]
        last = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    last = i
                else:
                    stack.pop()
                    if len(stack) == 0:
                        maxLen = max(maxLen, i-last)
                    else:
                        maxLen = max(maxLen, i - stack[-1])
        return maxLen
