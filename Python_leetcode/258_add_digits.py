class Solution(object):
    
    #accepted but cannot deal with negative number? 
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1 + (num-1)%9 if num else 0
        
    
    def addDigits_(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num != 0 and num %9 == 0:
            return 9
        return num%9
