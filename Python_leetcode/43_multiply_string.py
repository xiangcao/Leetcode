class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #1233*235
        len1, len2 = len(num1), len(num2)
        result=[0] * (len1+len2)
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                multiply = int(num1[-i1-1]) * int(num2[-i2-1]) 
                result[i1+i2] += multiply % 10
                result[i1+i2+1] += multiply /10 + result[i1+i2]/10
                result[i1+i2] = result[i1+i2] % 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return ''.join(str(digit)for digit in result[::-1])  
       # testcase "9133" "0"
       # testcase "0", "0"
        
