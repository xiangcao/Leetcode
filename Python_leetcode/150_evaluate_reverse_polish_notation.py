# a iterative solution: http://www.programcreek.com/2012/12/leetcode-evaluate-reverse-polish-notation/

class Solution(object):
    
    #Recursive solution
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #  Input: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]   Output: 12   Expected: 22 
        # the error is due to 6/-132 = -1 by python. 
        
        import operator
        map = {"+": operator.add, "-":operator.sub, "*":operator.mul, "/": operator.div}
        def calc(leftoperand, operator, rightoperand):
            if operator == "/":
                if (leftoperand < 0 and rightoperand > 0 ) or  (leftoperand > 0 and rightoperand < 0):
                    return -1 * map.get(operator)(abs(leftoperand), abs(rightoperand))
            return map.get(operator)(leftoperand, rightoperand)
        
        isoperator = lambda x: x in "+-*/"
        if isoperator(tokens[-1]):
            operator = tokens.pop()
            rightoperand = self.evalRPN(tokens)
            leftoperand = self.evalRPN(tokens)
            return calc(leftoperand, operator, rightoperand)
        else:
            operand = tokens.pop()
            return int(operand)
            
    #Iterative solution     
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
