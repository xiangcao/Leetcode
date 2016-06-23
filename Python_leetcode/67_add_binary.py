class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result=[]
        i = 0
        advance = 0 
        while i < len(a) and i < len(b):
            sum = int(a[-i-1]) + int(b[-i-1]) + advance
            result.append ( sum % 2)
            advance = sum / 2
            i += 1
        while i < len(a) or i < len(b) or advance: 
            toadd = int(a[-i-1]) if i < len(a) else int(b[-i-1]) if i < len(b) else 0
            sum = toadd + advance
            advance = sum/2
            result.append(sum % 2)
            i += 1
        return ''.join(str(i) for i in result[::-1])  #reverse
        # 11 + 11   110
        #Input: "1"   "1"
        #Output: "0"
        #Expected: "10" 
        # adding the least significant digit to the front of the result list       
