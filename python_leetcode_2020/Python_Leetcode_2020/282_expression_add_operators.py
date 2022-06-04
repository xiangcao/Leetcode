"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):
            # Done processing all the digits in num
            if index == N:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append(''.join(string[1:]))
                return
                        
            # Extending the current operand by one digit
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)
            
            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # NO OP recursion
                recurse(index+1, prev_operand, current_operand, value, string)
            
            # ADDITION
            string.append('+')
            string.append(str_op)
            recurse(index+1, current_operand, 0, value + current_operand, string)
            string.pop()
            string.pop()
            
            # Can subtract or multiply only if there are some previous operands
            if string:
                # SUBTRACTION
                string.append('-')
                string.append(str_op)
                recurse(index+1, -current_operand, 0, value - current_operand, string)
                string.pop()
                string.pop()
   
               # MULTIPLICATION
                string.append('*')
                string.append(str_op)
                recurse(index+1, current_operand * prev_operand, 0, value - prev_operand + prev_operand * current_operand, string)
                string.pop()
                string.pop()
                
            
        recurse(0, 0, 0, 0, [])
        return answers


# 2nd round
    #num: 105; target:5  10-5; 1*0 + 5
    #num: 232; target: 8;  2*3 + 2;  2 +3*2
    #num: 123; target: 6;  1+2+3; 1*2*3
    #num: 00, target: 0;  0*0; 0+0; 0-0;
    #num: "3456237490", target: 9191
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def dfs(index, expression, value, previous_operand):
            if index == len(num):
                if value == target:
                    result.append(expression)
                return
            for j in range(index, len(num)):
                operand_str = num[index:j+1]
                operand = int(operand_str)
                if index == 0:
                    dfs(j+1, expression+operand_str, operand, operand)
                else:
                    for operator in '+-*':
                        if operator =='+':
                            dfs(j+1, expression+operator+operand_str, value+operand, operand)
                        elif operator == '-':
                            dfs(j+1, expression+operator+operand_str, value-operand, -operand)
                        else: 
                            dfs(j+1, expression+operator+operand_str, value - previous_operand + previous_operand * operand, previous_operand * operand)            
                if operand_str == '0': # to avoid operand such as 05, 00, etc
                    break
        dfs(0, "", 0, 0)
        return result
