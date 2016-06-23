# 需要注意的点：
# 字符串处理，如果当前字符串是空格，或者其他特殊字符，要如何处理？ index要记得移动，不然就会进入死循环。
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        stack = []
        
        num = 0 
        sign = '+'
        for index in range(len(s)):
            ch = s[index]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if ( not ch.isdigit() and ch != ' ') or index == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/float(num)))
                num = 0
                sign = ch
        return sum(stack)
                
                
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # no use of stack
        
        if not s or len(s) == 0:
            return 0
        stack = []
        
        res = curres = 0
        sign = '+'
        
        pos = 0 
        while pos < len(s):
            if s[pos] == ' ':
                pos += 1
                continue
            temp = 0 
            if s[pos].isdigit():
                while pos < len(s) and s[pos].isdigit():
                    temp = temp*10 + int(s[pos])
                    pos += 1
                if sign == '+':
                    curres += temp
                if sign == '-':
                    curres -= temp
                if sign == '*':
                    curres *= temp
                if sign == '/':
                    curres = int(float(curres)/temp)
            else:
                if s[pos] == '+' or s[pos] == '-':
                    res += curres 
                    curres = 0
                sign = s[pos]
                pos += 1
        return res + curres
                
                
     # https://leetcode.com/discuss/42643/my-16-ms-no-stack-one-pass-short-c-solution 
