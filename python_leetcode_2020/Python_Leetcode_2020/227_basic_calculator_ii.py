"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7

"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        # s = s.replace(" ", "")
        length = len(s)
        res = 0
        preVal = 0 # initial preVal is 0
        sign = '+'; # initial sign is +
        i = 0
        while (i < length):
            if s[i] == ' ':
                i += 1
                continue
            curVal = 0
            while i < length and s[i].isdigit():
                curVal = curVal*10 + int(s[i])
                i += 1
            if sign == '+' or sign == '-':
                res += preVal # update res
                preVal = curVal if sign == '+' else -curVal
            elif (sign == '*'):
                preVal = preVal * curVal # not update res, combine preVal & curVal and keep loop
            elif (sign == '/'):
                preVal = int(float(preVal) / curVal) # not update res, combine preVal & curVal and keep loop
            if (i < length): # getting new sign
                sign = s[i]
                i += 1
        res += preVal
        return res
    
    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack, num, sign = [], 0, '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not (c.isspace() or c.isdigit()) or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)
                
    def calculate3(self, s):
        num, op, stack = 0, '+', [0]
        ops = {'+':lambda x, y: y, '-':lambda x, y: -y, '*':lambda x, y: x*y, '/':lambda x, y: (int)(float(x)/float(y))}
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s)-1:
                prev = 0 if op in '+-' else stack.pop()
                stack.append(ops[op](prev, num))
                num, op = 0, c
        return sum(stack)
  
class Solution:
    # "3+2*2"  7
    # "14-3/2"  13
    # " 3/2 "
    # " 3+5 / 2 "
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        i = 0
        value = 0
        operator = '+'
        s = ''.join(s.split(' '))
        while i < len(s):
            while i < len(s) and s[i].isdigit():
                value = value * 10 + int(s[i])
                i += 1
            if operator == '+':
                stack.append(value)
            elif operator == '-':
                stack.append(-value)
            elif operator == '*':
                stack.append(stack.pop() * value)
            else:
                stack.append(int(stack.pop()/value))
            value = 0
            if i == len(s):
                break
            operator = s[i]
            i += 1
        return sum(stack) 

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        i = 0
        value = 0
        operator = '+'
        #s = ''.join(s.split(' '))
        while i < len(s):
            while i < len(s) and s[i].isdigit():
                value = value * 10 + int(s[i])
                i += 1
            if i < len(s)-1 and s[i] == ' ':
                i += 1
                continue
            if operator == '+':
                stack.append(value)
            elif operator == '-':
                stack.append(-value)
            elif operator == '*':
                stack.append(stack.pop() * value)
            else:
                stack.append(int(stack.pop()/value))
            value = 0
            if i == len(s):
                break
            operator = s[i]
            i += 1
        return sum(stack)
