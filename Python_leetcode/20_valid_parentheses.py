class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        leftBracket="({["
        rightBracket=")}]"
        for i in s:
            if i in leftBracket:
                stack.append(i)
            elif i in rightBracket:
                if len(stack) == 0:
                    return False
                else:
                    l = stack.pop()
                    if rightBracket[leftBracket.index(l)] != i:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False
