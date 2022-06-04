"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Follow up: Could you solve the problem without using built-in library functions.
"""

class Solution:    
    # this is code for calculation II
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
    
    # recursively invoking the code from basic calculator II to handle bracket ()
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c 
            return sum(stack)
        return helper([], 0)
    
    # two stack; more complex; not recommended for interview
    def calculate(self, s: str) -> int:
		# first define a couple helper methods
		# operation helper to perform basic math operations
        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":  # integer division
                return first // second

		# calculate the relative precedence of the the operators "()" > "*/" > "+="
		# and determine if we want to do a pre-calculation in the stack
		# (when current_op is <= op_from_ops)
        def precedence(current_op, op_from_ops):
            if op_from_ops == '*' or op_from_ops == '/':
                return True
            if op_from_ops == '-' and current_op not in '*/':
                return True
            return False

        # also works
        def precedence(current_op, op_from_ops):

            if op_from_ops == "(" or op_from_ops == ")":
                return False
            if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True

        if not s:
            return 0
		# define two stack: nums to store the numbers and ops to store the operators
        nums, ops = [], []
        i = 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
                continue
            elif c.isdigit():
                num = int(c)
                while i < len(s) - 1 and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
            elif c == "(":
                ops.append(c)
            elif c == ")":
                # do the math when we encounter a ')' until '('
                while ops[-1] != "(":
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[-1]):
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(c)
            i += 1
        while len(ops) > 0:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
        return nums.pop()
