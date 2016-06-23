class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        def cal_no_bracket(expression):
            pos = 0
            sign = "+"
            res = 0 
            while pos < len(expression):
                if expression[pos] == " ": 
                    pos+=1
                    continue
                
                if expression[pos] == "+" or expression[pos] == "-":
                    sign = expression[pos]
                    pos += 1
                else:
                    tempRes = 0 
                    if expression[pos].isdigit():
                        while pos<len(expression) and expression[pos].isdigit():
                            tempRes = tempRes*10 + int(expression[pos])
                            pos += 1
                    
                    elif expression[pos] == "(":
                        pos, tempRes = calculateBracket(expression, pos+1)
                    if sign == "+":
                        res += tempRes
                    elif sign == "-":
                        res -= tempRes

            return res
        """
                
        def calculateBracket(expression, leftStartIndex):  
            pos = leftStartIndex
            res = 0 
            sign = "+"
            while pos < len(expression) and expression[pos] != ")":
                tempRes = 0 
                if expression[pos] == "(":
                    pos, tempRes = calculateBracket(expression, pos+1)
                else:
                    if expression[pos].isdigit():
                        while pos<len(expression) and expression[pos].isdigit():
                            tempRes = tempRes*10 + int(expression[pos])
                            pos += 1
                    else:
                        if expression[pos] == "+" or expression[pos] == "-":
                            sign = expression[pos]
                        pos += 1
                if sign == "+":
                    res += tempRes
                elif sign == "-":
                    res -= tempRes
    
            return pos+1, res

        #result  = cal_no_bracket(s)
        pos, result  = calculateBracket(s, 0)
        return result
        
        
    #Iterative: https://leetcode.com/discuss/39553/iterative-java-solution-with-stack
    # Next time practive solution using stack
    
    # https://leetcode.com/discuss/39532/easy-18-lines-c-16-lines-python  
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total
        
        
