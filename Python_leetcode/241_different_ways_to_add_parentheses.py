"""
https://leetcode.com/discuss/48468/11-lines-python
http://bookshadow.com/weblog/2015/07/27/leetcode-different-ways-add-parentheses/
https://leetcode.com/discuss/97307/java-simple-solution-beats-95%25

"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        curpath=[]
        result = []
    
        def calc(leftoperand, op, rightoperand):
            if op == "+":
                return int(leftoperand) + int(rightoperand)
            elif op == "-":
                return int(leftoperand) - int(rightoperand)
            elif op == "*":
                return int(leftoperand) * int(rightoperand)
            else:
                return int(rightoperand)

        def isoperator(ch):
            return ch == "+" or ch == "-" or ch == "*"
            
        # failed.  Input: "15-7*6+24"    Output: [-195,-51,240,72]    Expected: [-195,-51,-3,72,240] 
        # Input: "1+2+3"   Output: [6,6,6,6]   Expected: [6,6] 
        # Input: "15-7*6+24"  Output: [-195,-51,-51,240,240,72] Expected: [-195,-51,-3,72,240] 
        # Input: "15-7*6+24"  Output: [-195,-51,240,72]  Expected: [-195,-51,-3,72,240]      
        
        
        #Accepted
        def helper(input, curpath, index, result):
            if len(curpath) == len(input) and len(input)>1:
                return
            if len(input) == 3:
                result.append(calc(input[0], input[1], input[2]))
                return
            if index == len(input):
                rightoperand = curpath.pop()
                while len(curpath) > 1:
                    op = curpath.pop()
                    leftoperand = curpath.pop()
                    rightoperand = calc(leftoperand, op, rightoperand)
                result.append(int(rightoperand))
                return 
                    
            if isoperator(input[index]):
                curpath.append(input[index])
                index += 1
            
            # not process input[index]
            if index < len(input)-1 or len(curpath) ==0: # at least two more from input to process 
                helper(input, curpath+[input[index]], index+1, result)
            
            rightoperand = input[index]
            #process input[index]
            while len(curpath)>=2:
                op = curpath.pop()
                leftoperand = curpath.pop()
                #curpath.append(calc(leftoperand, op, input[index]))
                rightoperand = calc(leftoperand, op, rightoperand)
                if index < len(input)-1 or len(curpath) ==0:
                    helper(input, curpath+[rightoperand], index+1, result)

        
        splittedinput = []
        index1 = index2 = 0 
        while index2 < len(input):
            if isoperator(input[index2]):
                splittedinput.extend([input[index1:index2], input[index2]])
                index1 = index2+1
            index2 += 1
        splittedinput.append(input[index1:])

        helper(splittedinput, curpath, 0, result) 
        return result
                

                
    #Accepted
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
            
    #Accepted
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(input) if c in '+-*'
            for a in self.diffWaysToCompute(input[:i])
            for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
    #Accepted    
    def diffWaysToCompute(self, input):
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a,b) for i in xrange(lo, hi)
                                for a in build(lo, i)
                                for b in build(i+1, hi)]
        return build(0, len(nums)-1)
