"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

"""

class Solution(object):
# While there are operators remaining in the list, find the left-most operator. Apply it to the 2 numbers immediately before it, and replace all 3 tokens (the operator and 2 numbers) with the result.
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operand = {'+', '-', '*', '/'}
        def calculate(a, b, operand):
            if operand == '+':
                return a + b
            elif operand == '-':
                return a-b
            elif operand == '*':
                return a * b
            else:
                return int(1.0 * a/b)
        stack = []
        for token in tokens:
            if token in operand:
                number2 = stack.pop()
                number1 = stack.pop()
                stack.append(calculate(number1, number2, token))
            else:
                stack.append(int(token))
        return stack.pop()
                
                
